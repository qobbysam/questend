
FROM python:3
WORKDIR /code

RUN apt-get update && apt-get -y install   gcc musl-dev   libffi-dev    -y

RUN apt-get -y install  \
    gcc \
    musl-dev \
    libpq-dev python3-dev 

RUN apt-get update && apt-get install  -y g++ gcc libxslt-dev -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
#CMD [ "python", "liveserver.py" ]