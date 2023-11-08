#/bin/sh
if [ -z "${DOCKERACC}" ]; then
  echo "Set DOCKERACC env var with export DOCKERACC=<value>"
  exit
fi

kubectl -n semesterproject run kafka-publish --image=$DOCKERACC/kafka-publish
kubectl -n semesterproject run kafka-echo --image=$DOCKERACC/kafka-echo
