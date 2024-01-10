#!/bin/bash

docker stop myflix
docker rm myflix

bash ./rebuild.sh
docker run -dp 80:80 --name myflix flaskapp