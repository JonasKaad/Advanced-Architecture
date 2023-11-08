if [ -z "${DOCKERACC}" ]; then
  echo "Set DOCKERACC env var with export DOCKERACC=<value>"
  exit
fi

docker build -t kafka-publish .
docker image tag kafka-publish $DOCKERACC/kafka-publish:latest
docker image push $DOCKERACC/kafka-publish:latest
