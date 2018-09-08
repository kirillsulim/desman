#!/bin/bash
# Script to push container to docker repository

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push "$DOCKER_REPOSITORY"
