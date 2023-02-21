# Note: You can use any Debian/Ubuntu based image you want. 
FROM mcr.microsoft.com/devcontainers/python:3.7-bullseye

RUN \
    apt update && \
    apt-get install bash-completion graphviz default-mysql-client -y

ENV DJ_HOST localhost
ENV DJ_USER root
ENV DJ_PASS simple