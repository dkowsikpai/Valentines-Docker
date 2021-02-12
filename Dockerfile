FROM python
ENV PYTHONUNBUFFERED=1
WORKDIR /valentines
COPY requirements.txt /valentines/
RUN pip install -r requirements.txt
COPY . /valentines/

