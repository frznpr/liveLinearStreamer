from ffprobe import FFProbe


class Condition:
    @staticmethod
    def file_has_video_and_audio(file_path):
        fileMetadata = FFProbe(file_path)

        # Check if file has video and audio segment
        return (not fileMetadata.video) or (not fileMetadata.audio)
