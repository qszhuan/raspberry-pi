#!/usr/bin/env bash

NAME=$1

ps au | grep $NAME | awk '{print $2}' | xargs kill