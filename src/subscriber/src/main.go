package main

import (
	"fmt"
	"os"

	mqtt "github.com/eclipse/paho.mqtt.golang"
)

var connectHandler mqtt.OnConnectHandler = func(client mqtt.Client) {
    fmt.Println("Connected")
}

var connectLostHandler mqtt.ConnectionLostHandler = func(client mqtt.Client, err error) {
    fmt.Printf("Connect lost: %v", err)
}

func main() {
    var broker = "mosquitto"
    var port = 1883
    opts := mqtt.NewClientOptions()
    opts.AddBroker(fmt.Sprintf("tcp://%s:%d", broker, port))
    opts.OnConnect = connectHandler
    opts.OnConnectionLost = connectLostHandler
    
    receiveCount := 0
	choke := make(chan [2]string)

    opts.SetDefaultPublishHandler(func(client mqtt.Client, msg mqtt.Message) {
			choke <- [2]string{msg.Topic(), string(msg.Payload())}
	})

    client := mqtt.NewClient(opts)
    if token := client.Connect(); token.Wait() && token.Error() != nil {
        panic(token.Error())
    }

    if token := client.Subscribe("topic/lecture05", byte(0), nil); token.Wait() && token.Error() != nil {
        fmt.Println(token.Error())
        os.Exit(1)
    }

    for receiveCount < 5 {
        incoming := <-choke
        fmt.Printf("RECEIVED TOPIC: %s MESSAGE: %s\n", incoming[0], incoming[1])
        receiveCount++
    }
}
