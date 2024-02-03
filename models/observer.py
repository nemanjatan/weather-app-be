from utils.socketio import socketio


class Observer:
    def update(self, data):
        socketio.emit("weather_update", {"message": data})