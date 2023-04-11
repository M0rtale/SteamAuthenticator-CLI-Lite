FROM python:3.10-slim

RUN apt-get update && apt-get install -y socat
RUN pip3 install python-dotenv
RUN groupadd -r execu && useradd -r -g execu execu

WORKDIR /home/execu

ADD app.py .
RUN chmod 500 ./app.py
RUN chown execu:root . -R
ADD .env .
RUN chmod 444 .env

EXPOSE 6789
USER execu
CMD socat TCP-L:6789,fork,reuseaddr EXEC:"python3 app.py",pty,stderr,setsid,sane,raw,echo=0
