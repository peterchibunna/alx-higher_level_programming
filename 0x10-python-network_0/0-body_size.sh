#!/bin/bash
# Description of task
curl -sI "$1" | grep content-length | awk '{print $2}'
