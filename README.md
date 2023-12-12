# Group 14

Students:

- Victor Boye (`viboy20`)
- Sebastian Mondrup (`semon20`)
- Patrick Andreasen (`pandr20`)
- Rasmus Jacobsen (`rasmj20`)
- Jonas Solhaug Kaad (`jokaa17`)
- Alexander Nørup (`alnoe20`)

## Advanced Topics in Software Architecture project

The two experiments for the project can be found on the `src` folder. They can be found in their respective folders:
```
src
  ├── kafka_experiment
  └── mqtt_experiment
```

### MQTT Experiment

The MQTT experiment can be run with `docker compose up` or going into the `kubernetes-files` directory and running `kubectl apply -f .`, granted that you have Kubernetes config set up.

### Kafka Experiment

- **Prerequisite**: Have [Kafka](https://kafka.apache.org/downloads) installed in the cluster you want to run the experiment in.

The Kafka experiment can be run with `bash setup_experiment.sh`, as long as you have a Kubernetes config set up.

### Clean-up

- MQTT: `docker compose down` or `kubectl delete -f .`
- Kafka: `bash teardown_experiment.sh`
