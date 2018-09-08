#!/bin/bash
# Script to push desman to docker repository

if [ -n $1 ]; then
  TAG=$1
else
  exit 1
fi

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push kirillsulim/desman:$TAG
