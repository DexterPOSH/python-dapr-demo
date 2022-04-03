FROM python:3.10-slim as build
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
build-essential gcc 

WORKDIR /app
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.10-slim
WORKDIR /app
COPY --from=build /app/venv ./venv
COPY . .

ENV PATH="/app/venv/bin:$PATH"
CMD [ "python", "app.py" ]