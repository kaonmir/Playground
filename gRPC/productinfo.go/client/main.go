package main

import (
	"context"
	"flag"
	"log"
	"math/rand"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/protobuf/types/known/wrapperspb"

	pb "productinfo/protos"
)

var (
	addr = flag.String("addr", "localhost:50051", "the address to connect to")
)

func newRandomOrder(numFruit uint, id string) *pb.Order {
	rand.Seed(time.Now().Unix()) // initialize global pseudo random generator
	FRUITS := []string{"apple", "orange", "banana", "kiwi", "dragonfruit"}

	items := make([]string, numFruit)
	for i := 0; i < int(numFruit); i++ {
		items[i] = FRUITS[rand.Intn(len(FRUITS))]
	}

	return &pb.Order{Id: id, Items: items}
}

func addOrder(c pb.OrderManagementClient, ctx context.Context, numFruit uint) *wrapperspb.StringValue {
	order := newRandomOrder(numFruit, "")
	id, err := c.AddOrder(ctx, order)
	if err != nil {
		log.Fatalf("could not add order: %v", err)
		return nil
	}
	return id
}

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

	// Add Some Orders
	id1 := addOrder(c, ctx, 3)
	id2 := addOrder(c, ctx, 2)
	id3 := addOrder(c, ctx, 1)
	id4 := addOrder(c, ctx, 3)

	log.Print("Added Orders: " + id1.Value + ", " + id2.Value + ", " + id3.Value + ", " + id4.Value)

	// Get Order by Id
	/*
		order, err := c.GetOrder(ctx, id)
		if err != nil {
			log.Fatalf("could not get order: %v", err)
		}
		log.Print("GetOrder Response -> : ", order)
		orders, err := c.GetOrder(ctx, &wrappers.StringValue{Value: "106"})
	*/

	// Get Orders by Search Query
	/*
		searchStream, _ := c.SearchOrders(ctx, &wrappers.StringValue{Value: "banana"})
		for {
			searchOrder, err := searchStream.Recv()
			if err == io.EOF {
				break
			}
			log.Print("SearchOrder Response -> : ", searchOrder)
		}
	*/

	// Retrieve the order update stream
	updateStream, err := c.UpdateOrders(ctx)
	if err != nil {
		log.Fatalf("could not get order update stream: %v", err)
	}

	// Update Orders
	if err := updateStream.Send(newRandomOrder(3, id1.Value)); err != nil {
		log.Fatalf("%v.Send(%v) = %v", updateStream, id1, err)
	}

	if err := updateStream.Send(newRandomOrder(3, id2.Value)); err != nil {
		log.Fatalf("%v.Send(%v) = %v", updateStream, id2, err)
	}

	if err := updateStream.Send(newRandomOrder(4, id3.Value)); err != nil {
		log.Fatalf("%v.Send(%v) = %v", updateStream, id3, err)
	}

	updateRes, err := updateStream.CloseAndRecv()
	if err != nil {
		log.Fatalf("%v.CloseAndRecv() got 'error %v', want %v", updateStream, err, nil)
	}

	log.Printf("Update Orders Res : %s", updateRes.String())

}
