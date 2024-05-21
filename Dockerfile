# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN opentelemetry-bootstrap -a install

COPY . .

CMD export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true;opentelemetry-instrument --traces_exporter console --metrics_exporter console --logs_exporter console --service_name dice-server;python3 -m flask run --host=0.0.0.0