FROM python:3.7.2-slim

COPY . /app
WORKDIR /app


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_DEBUG=1
ENV FLASK_APP=app.py

ENTRYPOINT ["python", "app.py"]