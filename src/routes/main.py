from routes.api import *

def add_routes(app):

    app.add_route(stream_video, "/stream/<content_params>",
                  methods=['GET'], name='api.stream_video')
