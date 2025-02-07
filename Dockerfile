FROM docker.arvancloud.ir/python:3.11.2-alpine

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "-m", "app.main" ]