from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from prometheus_client import start_http_server
from random import randint
from flask import Flask
import logging
import os

# Setup - create a metric reader with a meter
prefix = "DiceRoller"
reader = PrometheusMetricReader(prefix)
metrics.set_meter_provider(MeterProvider(metric_readers=[reader]))
meter = metrics.get_meter_provider().get_meter("diceroller.meter")

# Now create a counter instrument to make measurements with
roll_counter = meter.create_counter(
    "dice.rolls",
    description="The number of rolls by roll value",
)

# Start the flask app with logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/")
def roll_dice():
    # Roll the dice (random number 1-6)
    result = str(roll())

    # Count the dice roll against a tally for that value
    roll_counter.add(1, {"roll.value": result})

    # Log the dice roll
    logger.info("Player is rolling the dice: %s", result)

    return result


def roll():
    return randint(1, 6)


if __name__ == "__main__":
    # Start Prometheus metrics server
    start_http_server(9001)

    # Run the Flask app
    flask_host = "0.0.0.0" if 'FLASK_BIND_ALL' in os.environ else "localhost"
    app.run(host=flask_host, port=9000)
