from sanic import response
from app.handlers.streamHandler import StreamHandler


async def stream_video(request, playlist_name):
    """
    Get request and call relevant request handler

    @param request:
    @param playlist_name:
    @return json:
    """

    stream_handler = StreamHandler()
    action = await stream_handler.stream_playlist(playlist_name)

    return response.json(action)
