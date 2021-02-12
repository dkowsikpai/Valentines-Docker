FROM python:3.6
ENV PYTHONUNBUFFERED=1
WORKDIR /valentines
COPY requirements.txt /valentines/
RUN pip install -r requirements.txt
COPY . /valentines/

