
FROM golang:1.21.1

WORKDIR /usr/src/subscriber

COPY go.mod go.sum ./

RUN go mod download

COPY  ./src/main.go ./

RUN CGO_ENABLED=0 GOOS=linux go build -o /docker-gs-ping
CMD ["/docker-gs-ping"]