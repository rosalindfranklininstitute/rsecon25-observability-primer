from random import randint
from flask import Flask
import logging
import os

# Create the flask app with logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/")
def roll_dice():
    # Roll the dice (random number 1-6)
    result = str(roll())

    # Log the dice roll
    logger.info("Player is rolling the dice: %s", result)

    return result


def roll():
    return randint(1, 6)


if __name__ == "__main__":
    # Run the Flask app
    flask_host = "0.0.0.0" if 'FLASK_BIND_ALL' in os.environ else "localhost"
    app.run(host=flask_host, port=9000)
