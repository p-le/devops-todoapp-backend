FROM python:3.9-slim
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
ENV PORT 8080

WORKDIR $APP_HOME

RUN pip install --no-cache-dir poetry
COPY . /app
RUN poetry install

EXPOSE 8080

CMD poetry run uvicorn fastapi_todoapp.main:app --host 0.0.0.0 --port $PORT 