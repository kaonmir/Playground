package main

import (
	"context"
	"io"
	"log"
	pb "productinfo/protos"
	"time"
)

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

// Senario 1: Add Orders
func Senario1(ctx context.Context, c pb.OrderManagementClient) {
	for i := 0; i < 6; i++ {
		_ = AddOrder(c, ctx, 3)
	}
}

// Senario 2: Add and Get Order
func Senario2(ctx context.Context, c pb.OrderManagementClient) {
	for i := 0; i < 2; i++ {
		id := AddOrder(c, ctx, 3)
		order, err := c.GetOrder(ctx, id)
		if err != nil {
			log.Fatalf("could not get order: %v", err)
		}
		log.Printf("Adding order: %v", order)
	}
}

// Senario 3: Process Orders
func Senario3(ctx context.Context, c pb.OrderManagementClient) {
	processStream, err := c.ProcessOrders(ctx)
	if err != nil {
		log.Fatalf("could not process orders: %v", err)
	}

	for i := 0; i < 10; i++ {
		time.Sleep(time.Millisecond * 300)
		if err := processStream.Send(NewRandomOrder(3, "")); err != nil {
			log.Fatalf("%v.Send = %v", processStream, err)
		}
	}

	channel := make(chan struct{})
	go asyncBidirectionalRPC(processStream, channel)

	processStream.CloseSend()
	<-channel
}
