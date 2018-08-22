#!/bin/bash

# script to build docker image with examples

TMP=$(mktemp -d)

cat << EOF > $TMP/Dockerfile
FROM python:3.7-alpine
WORKDIR /examples
RUN pip install kubernetes_asyncio
COPY examples/in_cluster_config.py /examples/
CMD ["python", "/examples/in_cluster_config.py"]
EOF

cp -r examples $TMP/
docker build -t tpimages/kubernetes_asyncio_examples:latest $TMP

rm -fr $TMP
