FROM python:3.8.5
MAINTAINER vikrant
WORKDIR /devop
ADD . /devop
EXPOSE 4000
CMD ["python","calculator.py"]
