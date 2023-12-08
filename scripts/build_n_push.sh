#!/bin/bash

VERSION_TAG=$1

cd ../app

# without buildx
# docker build -t ashraftheminhaj/hushhub-frontend:$1 .
# docker tag ashraftheminhaj/hushhub-frontend:$1 ashraftheminhaj/hushhub-frontend:latest
# docker push ashraftheminhaj/hushhub-frontend:$1 

# with buildx
docker buildx create --use --platform=linux/arm64,linux/amd64 --name multiplatform-builder
# docker buildx inspect --bootstrap
docker buildx build --platform=linux/arm64,linux/amd64 --push --tag ashraftheminhaj/hushhub-frontend:$1 .