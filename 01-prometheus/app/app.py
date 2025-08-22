from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Counter

from random import randint
from flask import Flask
import logging
import os

# Start the flask app with logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

# Create a counter instrument to make measurements with
roll_counter = Counter(
    "dice_rolls",
    "The number of rolls by roll value",
    ["roll_value"]
)


@app.route("/")
def roll_dice():
    # Roll the dice (random number 1-6)
    result = str(roll())

    # Count the dice roll against a tally for that value
    roll_counter.labels(roll_value=result).inc()

    # Log the dice roll
    logger.info("Player is rolling the dice: %s", result)

    return result


def roll():
    return randint(1, 6)


if __name__ == "__main__":
    # Run the Flask app
    flask_host = "0.0.0.0" if 'FLASK_BIND_ALL' in os.environ else "localhost"
    app.run(host=flask_host, port=9000)
