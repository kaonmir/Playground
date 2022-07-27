package main

import (
	"context"
	"flag"
	"io"
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
	DESTINATION := []string{"US", "UK", "India", "China"}

	items := make([]string, numFruit)
	for i := 0; i < int(numFruit); i++ {
		items[i] = FRUITS[rand.Intn(len(FRUITS))]
	}
	destination := DESTINATION[rand.Intn(len(DESTINATION))]

	return &pb.Order{Id: id, Items: items, Destination: destination}
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

func asyncBidirectionalRPC(processStream pb.OrderManagement_ProcessOrdersClient, c chan struct{}) {
	for {
		combinedShipment, err := processStream.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatalf("could not receive combined shipment: %v", err)
		}
		log.Printf("Combined Shipment received: {Destination: %v, OrderList: %d}", combinedShipment.Destination, len(combinedShipment.OrdersList))
	}
	c <- struct{}{}
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
	ctx, cancel := context.WithTimeout(context.Background(), time.Second*10)
	defer cancel()

	// Process Orders and Retrieve the combined shipment
	processStream, err := c.ProcessOrders(ctx)
	if err != nil {
		log.Fatalf("could not process orders: %v", err)
	}

	channel := make(chan struct{})
	go asyncBidirectionalRPC(processStream, channel)

	// for 6 times process Stream
	for i := 0; i < 10; i++ {
		time.Sleep(time.Millisecond * 300)
		if err := processStream.Send(newRandomOrder(3, "")); err != nil {
			log.Fatalf("%v.Send = %v", processStream, err)
		}
	}

	processStream.CloseSend()
	<-channel
}
