FROM python:3.8-slim-buster

WORKDIR /

COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install default-libmysqlclient-dev --assume-yes
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=3000"]