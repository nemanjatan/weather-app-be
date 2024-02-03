# Weather App Backend

This project implements a backend for a weather notification service using Flask and Socket.IO, demonstrating the Observer Pattern in software design.

## Project Structure

- `models/`: Contains the Observer and Subject classes for implementing the Observer Pattern.
  - `observer.py`: Defines the base `Observer` class.
  - `rain_observer.py`: Extends `Observer` to react specifically to rain alerts.
  - `subject.py`: Implements the `Subject` class to manage observers.
- `routes/`: Flask routes for subscribing and unsubscribing to weather alerts.
  - `subscription.py`: Handles subscription management.
- `utils/`: Utility scripts and configurations.
  - `socketio.py`: Configures Socket.IO for real-time web communication.
  - `weather.py`: Contains the logic to check current weather conditions using the OpenWeather API.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Set up your OpenWeather API key in `utils/weather.py`.
3. Run the backend server: `python main.py`


## Usage

- **Subscribe to alerts:** Send a POST request to `/api/subscribe` with an observer ID and alert type.
- **Unsubscribe from alerts:** Send a POST request to `/api/unsubscribe` with the observer ID.
- **Trigger weather check:** Access `/api/notify` to manually trigger a check for current weather conditions.

## Front-end Project
This backend is designed to work seamlessly with its React Native front-end counterpart, which provides a user interface for subscribing to weather alerts and receiving real-time notifications. The front-end application utilizes Socket.IO for real-time communication with this backend, demonstrating a complete system that leverages the Observer Pattern for delivering weather updates to users.

Check out the front-end project here: [Weather App Front-end](https://github.com/nemanjatan/weather-app/)

## Contributing

Contributions to the project are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open-sourced under the MIT License.
