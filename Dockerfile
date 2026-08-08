FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

WORKDIR /action
COPY action/entry.py /action/entry.py
COPY requirements.txt /action/requirements.txt

ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["python", "/action/entry.py"]
