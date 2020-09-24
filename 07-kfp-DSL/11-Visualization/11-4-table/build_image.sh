#!/bin/bash -e
image_name=hanjoo8821/table
image_tag=ex
full_image_name=${image_name}:${image_tag}

cd "$(dirname "$0")"
docker build -t "${full_image_name}" .
docker push "$full_image_name"