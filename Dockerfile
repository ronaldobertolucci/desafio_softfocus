FROM python:3.9.12-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /desafio_softfocus

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
