#!/bin/bash
# Script to push desman to docker repository

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push kirillsulim/desman
