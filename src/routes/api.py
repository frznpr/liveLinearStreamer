from app.controllers.streamController import stream_video as stream_video_controller

async def stream_video(request, content_params):
    return await stream_video_controller(request, content_params)
