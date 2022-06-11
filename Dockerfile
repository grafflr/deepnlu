FROM python:3.8.5

RUN apt-get update && apt-get upgrade -y
RUN apt install -y curl

# Install and setup poetry
RUN pip install -U pip \
    && apt-get update \
    && apt install -y curl netcat \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
ENV PATH="${PATH}:/root/.poetry/bin"


COPY . /deepnlu

#ENV GRAFFLR_HOME="/home/ubuntu/graffl-core"
#ENV GRAFFLR_HOME="/graffl-core"

WORKDIR /deepnlu
RUN make all

#WORKDIR /graffl-core/apps/runners/slackbot
#RUN make build

##CMD './scripts/run-loqibot.sh'