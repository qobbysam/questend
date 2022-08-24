
FROM python:3.8.6-alpine
WORKDIR /code

RUN apk --update --upgrade add --no-cache  gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip install --no-cache-dir psycopg2 \
    && apk del --no-cache .build-deps
RUN apk add --update --no-cache g++ gcc libxslt-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
#CMD [ "python", "liveserver.py" ]