# syntax=docker/dockerfile:1.4
FROM python:3.10-alpine

WORKDIR /backend
COPY --chmod=765 . /backend
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]