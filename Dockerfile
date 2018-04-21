FROM debian:latest

RUN apt-get update -y
RUN apt-get install python3 python3-pip mpd -y
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD . ayydio

CMD [ "/bin/bash", "ayydio/start.sh" ]