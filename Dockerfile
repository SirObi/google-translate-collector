FROM python:3.7.0-alpine3.8
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev
RUN apk add openssl-dev
RUN pip install cryptography==2.2.2
RUN pip install --no-cache-dir --trusted-host pypi.python.org pipenv
RUN mkdir /app
WORKDIR /app
COPY Pipfile ./
RUN pipenv install
CMD echo "Hello world"
