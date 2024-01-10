#!/bin/bash

docker image rm flaskapp
docker build -t flaskapp .