package main

import (
	"errors"
	"fmt"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

var (
	// ErrNoIP No IP found in response
	ErrNoIP = errors.New("No IP in HTTP response")

	// ErrNon200Response non 200 status code in response
	ErrNon200Response = errors.New("Non 200 Response found")
)

type Body struct {
	FirstName string `json:"firstName"`
	LastName  string `json:"lastName"`
}

func handler(event Body) (events.APIGatewayProxyResponse, error) {
	return events.APIGatewayProxyResponse{
		Body:       fmt.Sprintf("Hello, %v", event.FirstName+" "+event.LastName),
		StatusCode: 200,
	}, nil
}

func main() {
	lambda.Start(handler)
}
