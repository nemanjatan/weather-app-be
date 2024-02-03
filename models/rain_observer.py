from models.observer import Observer


class RainObserver(Observer):
    def __init__(self, id, alert_type):
        self.id = id
        self.alert_type = alert_type

    def update(self, data):
        print(f"Observer {self.id} notified about {self.alert_type} with message: {data}")
        super().update(data)