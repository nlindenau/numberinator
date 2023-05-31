#!/bin/sh

docker build -t cloud-mw -f src/cloud_middleware/docker/Dockerfile ./src/cloud_middleware

docker build -t server -f src/server/docker/Dockerfile ./src/server

docker build -t frontend -f src/frontend/docker/Dockerfile ./src/frontend