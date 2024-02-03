from flask import Flask

from routes.subscription import subscription_blueprint
from utils.socketio import socketio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'youtube-tutorial'
app.register_blueprint(subscription_blueprint, url_prefix='/api')

socketio.init_app(app)


@socketio.on("connect")
def connected():
    print("client has connected")


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)