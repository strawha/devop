FROM python:3.8.5
MAINTAINER vikrant
WORKDIR /calculator
ADD . /calculator
EXPOSE 4000
CMD ["python","calc.py"]
