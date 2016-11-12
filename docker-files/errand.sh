#!/usr/bin/env bash

# rm not used docker container
docker ps -a | grep 'weeks ago' | awk '{print $1}' | xargs docker rm
