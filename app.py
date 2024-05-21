from flask import Flask
import logging

from opentelemetry.sdk.resources import SERVICE_NAME, Resource

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter

# Service name is required for most backends,
# and although it's not necessary for console export,
# it's good to set service name anyways.
resource = Resource(attributes={
    SERVICE_NAME: "Opentelemetry Sample"
})

traceProvider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())
traceProvider.add_span_processor(processor)
trace.set_tracer_provider(traceProvider)

reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
meterProvider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(meterProvider)

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def welcome():
    return "Welcome to Opentelemetry-sample"
