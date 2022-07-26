package main

import (
	"context"
	"flag"
	"log"
	"time"

	"github.com/golang/protobuf/ptypes/wrappers"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"

	pb "productinfo/protos"
)

const (
	defaultName = "world"
)

var (
	addr = flag.String("addr", "localhost:50051", "the address to connect to")
)

func main() {
	flag.Parse()
	// Set up a connection to the server.
	conn, err := grpc.Dial(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	// c := pb.NewProductInfoClient(conn)
	c := pb.NewOrderManagementClient(conn)

	// Contact the server and print out its response.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	retrievedOrder, err := c.GetOrder(ctx, &wrappers.StringValue{Value: "106"})
	if err != nil {
		log.Fatalf("could not get order: %v", err)
	}
	log.Print("GetOrder Response -> : ", retrievedOrder)

	/*
		r, err := c.AddProduct(ctx, &pb.Product{Id: *id, Name: *name, Price: 100.0})
		if err != nil {
			log.Fatalf("could not add product: %v", err)
		}

		product, err := c.GetProduct(ctx, r)
		if err != nil {
			log.Fatalf("could not get product: %v", err)
		}
		log.Printf("Product: %+v\n", product)
	*/
}
