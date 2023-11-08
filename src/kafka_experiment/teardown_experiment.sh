#/bin/sh

kubectl delete pod kafka-publish -n semesterproject
kubectl delete pod kafka-echo -n semesterproject
