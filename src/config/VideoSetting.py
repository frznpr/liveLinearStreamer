class VideoSetting:

    RTMP_SERVER_ULR = 'rtmp://hls-streamer/show/'

    SUPPORTED_VIDEO_FORMATS = [
        {
            'name': '480',
            'width': '854',
            'height': '480',
            'videoBitrate': '1250K',
            'audioBitrate': '128k',
            'frameRate': '25',
            'crf': '23',
        },
        {
            'name': '720',
            'width': '1280',
            'height': '720',
            'videoBitrate': '2500K',
            'audioBitrate': '128k',
            'frameRate': '25',
            'crf': '23',
        },
    ]
