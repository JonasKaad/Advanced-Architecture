if [ -z "${DOCKERACC}" ]; then
  echo "Set DOCKERACC env var with export DOCKERACC=<value>"
  exit
fi

docker build -t kafka-echo .
docker image tag kafka-echo $DOCKERACC/kafka-echo:latest
docker image push $DOCKERACC/kafka-echo:latest
