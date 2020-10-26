#!/bin/sh
docker build -t my-prometheus .
docker run -d -p 9090:9090 --net=host my-prometheus
docker run -d -p 3000:3000 --net=host grafana/grafana
docker run -d -p 9100:9100 -v "/:/hostfs" --net=host prom/node-exporter --path.rootfs=/hostfs --collector.textfile.directory=/hostfs/tmp
