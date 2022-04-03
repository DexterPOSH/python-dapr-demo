FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip &&  pip install /app/requirements.txt
ENTRYPOINT ["python"]
EXPOSE 8080
CMD ["app.py"]