
FROM python:3
WORKDIR /code

RUN apt-get update && apt-get install --no-cache  gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN apt-get install --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    geos\
    && pip install --no-cache-dir psycopg2 \
RUN apt-get update && apt-get install  g++ gcc libxslt-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
#CMD [ "python", "liveserver.py" ]