FROM python:3.8.5
MAINTAINER vikrant1strawha
WORKDIR /devop
ADD . /devop
EXPOSE 4000
CMD ["python","devop.py"]
