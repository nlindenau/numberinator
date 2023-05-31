#!/bin/sh

docker build -t cloud-mw -f src/cloud_middleware/docker/Dockerfile ./src/cloud_middleware

docker build -t cloud-mw -f src/cloud_middleware/docker/Dockerfile ./src/cloud_middleware