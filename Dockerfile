FROM python:3.7.0-alpine3.8
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev
RUN apk add openssl-dev
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh
RUN pip install cryptography==2.2.2
RUN pip install --no-cache-dir --trusted-host pypi.python.org pipenv
RUN mkdir /app
WORKDIR /app
COPY Pipfile ./
COPY Pipfile.lock ./
RUN pipenv install
RUN pipenv install keyring
COPY helpers.py ./
COPY create_recording.py ./
COPY to_speech_bing.py ./
COPY csv_inputs ./csv_inputs
RUN mkdir json_files
COPY mp3_outputs ./mp3_outputs
COPY silence_mp3s ./silence_mp3s
CMD ["python", "to_speech_bing.py"]
