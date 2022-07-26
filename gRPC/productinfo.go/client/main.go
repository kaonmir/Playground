package main

import (
	"context"
	"flag"
	"log"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"

	pb "productinfo/protos"
)

const (
	defaultName = "world"
)

var (
	addr = flag.String("addr", "localhost:50051", "the address to connect to")
	id   = flag.String("id", "1", "Id for product")
	name = flag.String("name", defaultName, "Name for product")
)

func main() {
	flag.Parse()
	// Set up a connection to the server.
	conn, err := grpc.Dial(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewProductInfoClient(conn)

	// Contact the server and print out its response.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	r, err := c.AddProduct(ctx, &pb.Product{Id: *id, Name: *name, Price: 100.0})
	if err != nil {
		log.Fatalf("could not add product: %v", err)
	}

	product, err := c.GetProduct(ctx, r)
	if err != nil {
		log.Fatalf("could not get product: %v", err)
	}
	log.Printf("Product: %+v\n", product)
}
