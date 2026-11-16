#!/bin/bash

docker network create tplb
docker build -t im-nginx-lb ./tp-A

mkdir -p shared1 shared2
echo "<h1>Hello 1</h1>" > shared1/index.html
echo "<h1>Hello 2</h1>" > shared2/index.html

docker run -d --name nginx1 --rm -p 81:80 -v "$(pwd)/shared1:/usr/share/nginx/html" --network tplb nginx:latest
docker run -d --name nginx2 --rm -p 82:80 -v "$(pwd)/shared2:/usr/share/nginx/html" --network tplb nginx:latest

docker run -d --name nginx-lb --rm -p 83:80 --network tplb im-nginx-lb

