from app.actions.action import Action
from config.VideoSetting import VideoSetting
from ffmpy3 import FFmpeg
from string import Template
from sanic.exceptions import ServerError
from sanic.log import logger


class StreamAction(Action):

    # Ffmpeg complex format template
    FILTER_COMPLEX_FRAGMENT = [
        '[$i:v]scale=$width:$height:force_original_aspect_ratio=1,setsar=1:1[v$i]; ',
        '[v$i]pad=$width:$height:($width-iw)/2:($height-ih)/2:color=blue[vp$i]; ',
        '[vp$i][$i:a]',
    ]

    async def rtmp_stream(self, playlist_name, filePathList):
        """
        Normalise and concat list of video files

        @param playlist_name:
        @param filePathList:
        @return Streaming start result:
        """
        try:
            input_count = len(filePathList)
            outputs = {}

            # Generate output segment for each supported format and resolution like 480p ,720p
            for format in VideoSetting.SUPPORTED_VIDEO_FORMATS:

                # Put variables in filter complex template for each output resolution
                formatFilter = ''
                for templateText in self.FILTER_COMPLEX_FRAGMENT:

                    scaleFilter = ''
                    for i, input in enumerate(filePathList):
                        template = Template(templateText)
                        scaleFilter += template.substitute(i=i, width=format['width'], height=format['height'])
                    formatFilter += scaleFilter

                # Create FFmpeg output command
                outputs[VideoSetting.RTMP_SERVER_ULR + playlist_name + '_' + format['name']] = \
                    '-filter_complex "' + formatFilter + \
                    f'concat=n={input_count}:v=1:a=1[v][a] " ' + \
                    '-map "[v]" -map "[a]" ' + \
                    f'-c:v libx264 -c:a aac -b:v {format["videoBitrate"]} -b:a {format["audioBitrate"]} -r {format["frameRate"]}  ' + \
                    f'-tune zerolatency -preset veryfast -crf {format["crf"]} -f flv'

            # Sets ffmpeg variables
            ff = FFmpeg(
                inputs={filePath: '-re' for filePath in filePathList},
                outputs=outputs
            )
            logger.info(f'Ffmpeg Command:  {ff.cmd}')

            # Run ffmpeg in async mode
            await ff.run_async()

            return {'Streaming': 'Started'}

        except:
            raise ServerError({'Streaming': 'Error'}, status_code=500)
