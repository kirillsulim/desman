#!/bin/sh
# Run desman from docker container

set -e

NAME=""
VERSION="1.0.0"
IMAGE="$NAME:$VERSION"

# Setup volume mounts
if [ "$(pwd)" != '/' ]; then
    VOLUMES="-v $(pwd):$(pwd)"
fi
if [ -n "$HOME" ]; then
    VOLUMES="$VOLUMES -v $HOME:$HOME"
fi

# Allocate tty if any exists
if [ -t 0 ]; then
    if [ -t 1 ]; then
        DOCKER_RUN_OPTIONS="$DOCKER_RUN_OPTIONS -t"
    fi
else
    DOCKER_RUN_OPTIONS="$DOCKER_RUN_OPTIONS -i"
fi

exec docker run --rm $DOCKER_RUN_OPTIONS $VOLUMES -w "$(pwd)" $IMAGE "$@"
