ARG PY_VER
ARG DISTRO
FROM mcr.microsoft.com/devcontainers/python:${PY_VER}-${DISTRO}

RUN \
    # dev setup
    apt update && \
    apt-get install sudo git gcc bash-completion graphviz default-mysql-client -y && \
    pip install --no-cache-dir --upgrade black faker ipykernel pip && \
    apt-get clean

# tutorial dependencies
COPY ./requirements.txt /tmp/
RUN \
    pip install --no-cache-dir -r /tmp/requirements.txt --upgrade && \
    rm /tmp/requirements.txt

USER root
ENV DJ_HOST db
ENV DJ_USER root
ENV DJ_PASS simple
