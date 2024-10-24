FROM docker.arvancloud.ir/python:3.9.20-bookworm

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app/main.py" ]