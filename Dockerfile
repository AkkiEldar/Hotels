FROM python:3.10-alpine
WORKDIR /hotel/
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt /hotel/
RUN pip install -r requirements.txt
COPY . /hotel/
