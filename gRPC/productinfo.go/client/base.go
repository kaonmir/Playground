package main

import (
	"context"
	"log"
	"math/rand"
	pb "productinfo/protos"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/protobuf/types/known/wrapperspb"
)

func NewOrderManagementClient() (*grpc.ClientConn, context.Context, context.CancelFunc, pb.OrderManagementClient) {
	// Set up a connection to the server.
	conn, err := grpc.Dial(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}

	// Contact the server and print out its response.
	// ctx, cancel := context.WithTimeout(context.Background(), time.Second*3)
	ctx, cancel := context.WithDeadline(context.Background(), time.Now().Add(time.Duration(time.Second*1)))

	c := pb.NewOrderManagementClient(conn)

	return conn, ctx, cancel, c
}

func AddOrder(c pb.OrderManagementClient, ctx context.Context, numFruit uint) *wrapperspb.StringValue {
	order := NewRandomOrder(numFruit, "")
	id, err := c.AddOrder(ctx, order)
	if err != nil {
		log.Fatalf("could not add order: %v", err)
		return nil
	}
	return id
}

func NewRandomOrder(numFruit uint, id string) *pb.Order {
	rand.Seed(time.Now().Unix()) // initialize global pseudo random generator
	FRUITS := []string{"apple", "orange", "banana", "kiwi", "dragonfruit"}
	DESTINATION := []string{"US", "UK", "India", "China"}

	items := make([]string, numFruit)
	for i := 0; i < int(numFruit); i++ {
		items[i] = FRUITS[rand.Intn(len(FRUITS))]
	}
	destination := DESTINATION[rand.Intn(len(DESTINATION))]

	return &pb.Order{Id: id, Items: items, Destination: destination}
}
