from sanic import Sanic
from routes.main import add_routes
from config.SanicSetting import SanicSetting

app = Sanic('Pterosaurs')
app.config.from_object(SanicSetting)
add_routes(app)

app.run(
    host=SanicSetting.ENV['host'],
    port=SanicSetting.ENV['port'],
    debug=SanicSetting.ENV['debug'],
    workers=SanicSetting.ENV['workers'],
    access_log=SanicSetting.ENV['access_log'],
)
