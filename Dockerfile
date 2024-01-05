FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
ENV NAME reservations_api
CMD ["python", "app.py"]