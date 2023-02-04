# Dockerfile to build a flask app

FROM python:3.9
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000

CMD ["python","Flask_api.py"] ####