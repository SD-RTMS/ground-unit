#!/bin/sh
docker build -t my-prometheus .
docker run -d -p 3000:3000 --net=host --user=0:0 --volume "$PWD/grafana:/var/lib/grafana" grafana/grafana
docker run -d -p 9100:9100 -v "/:/hostfs" --net=host prom/node-exporter --path.rootfs=/hostfs
docker run -d -p 9091:9091 --net=host prom/pushgateway
docker run -d -p 9090:9090 --net=host --user=0:0 --volume "$PWD/prom:/prometheus" my-prometheus
