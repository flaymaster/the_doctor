FROM python:3.10-slim

WORKDIR /app

COPY app/main.py /app/

RUN pip install --no-cache-dir flask boto3 python-dotenv

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

CMD ["flask", "run"]