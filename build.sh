#!/bin/bash
set -e
cd "$(dirname "$0")"

docker build --pull -t fontcustom:latest .

rm -f .fontcustom-manifest.json
docker run --rm -ti -v $PWD:/work -u "$(id -u):$(id -g)" -w /work fontcustom:latest fontcustom compile
