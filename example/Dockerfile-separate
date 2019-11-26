FROM alpine:3.10
MAINTAINER Oscar Rubio Garcia 

WORKDIR /code

RUN apk update && apk upgrade 
RUN apk add --update py-pip
RUN apk add linux-headers python3 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code

CMD [ "gunicorn", "-b", "0.0.0.0:5000", "app:api", "--reload" ]

