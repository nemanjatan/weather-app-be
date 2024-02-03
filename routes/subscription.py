from flask import Blueprint, request

from models.rain_observer import RainObserver
from models.subject import Subject
from utils.weather import get_current_weather

subscription_blueprint = Blueprint("subscription_blueprint", __name__)
subject = Subject()


@subscription_blueprint.route("/subscribe", methods=["POST"])
def subscribe():
    observer_id = request.json.get("id")
    alert_type = request.json.get("alert_type")
    if alert_type == "rain":
        observer = RainObserver(observer_id, alert_type)
        subject.attach(observer)
    return "Observer added for alert type: " + alert_type, 200


@subscription_blueprint.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    observer_id = request.json.get("id")
    observer_to_remove = next((
        obs for obs in subject._observers if obs.id == observer_id
    ), None)

    if observer_to_remove:
        subject.detach(observer_to_remove)
        return "Observer " + observer_id + " removed", 200
    return "Observer " + observer_id + " not found", 404


@subscription_blueprint.route('/notify', methods=['GET'])
def notify():
    if get_current_weather():
        subject.notify("⛈️ Rain expected in 30 minutes.")
        return "Rain detected, sending notification", 200
    else:
        return "No rain detected, skipping notification...", 200
