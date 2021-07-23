import glob
import logging
import os

from app.actions.streamAction import StreamAction
from app.conditions.condition import Condition
from app.handlers.handler import Handler
from config.path import Path


class StreamHandler(Handler):

    async def stream_playlist(self, playlist_name):
        """
        This handler act as a decision making method, which pass and get data from actions.
        @param playlist_name:
        @return: streamer action result
        """
        playlist_path = Path.STORAGE_PATH + Path.ORIGINAL_PATH + playlist_name

        # Search in playlist folder with the same name as input.
        if not os.path.isdir(playlist_path):
            logging.debug(playlist_path)
            action = StreamAction()
            return await action.playlist_not_found()

        # Create playlist file path
        playlistFiles = []
        for file_path in sorted(glob.iglob(playlist_path + '/*.*')):

            # Check if file has video and audio segment
            if Condition.file_has_video_and_audio(file_path):
                logging.debug(f'Video and/or audio is missing in {file_path}')
            else:
                playlistFiles.append(file_path)

        if not playlistFiles:
            action = StreamAction()
            return await action.playable_video_not_found()

        # Start streaming
        stream_action = StreamAction()
        return await stream_action.rtmp_stream(playlist_name, playlistFiles)
