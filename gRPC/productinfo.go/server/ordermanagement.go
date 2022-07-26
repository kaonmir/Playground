package main

import (
	"context"
	"fmt"
	"io"
	"log"
	pb "productinfo/protos"
	"strings"

	"github.com/gofrs/uuid"
	"github.com/golang/protobuf/ptypes/wrappers"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

type OrderManagement struct {
	pb.UnimplementedOrderManagementServer
	orderMap map[string]*pb.Order
}

func (m *OrderManagement) GetOrder(ctx context.Context, in *wrappers.StringValue) (*pb.Order, error) {
	log.Print("Get order " + in.Value)

	if m.orderMap[in.Value] == nil {
		return nil, status.Errorf(codes.NotFound, "Order not found", in.Value)
	}

	ord := m.orderMap[in.Value]
	return ord, status.New(codes.OK, "Order found").Err()
}

func (m *OrderManagement) SearchOrders(searchQuery *wrappers.StringValue, stream pb.OrderManagement_SearchOrdersServer) error {
	for key, order := range m.orderMap {
		for _, itemStr := range order.Items {
			if strings.Contains(itemStr, searchQuery.Value) {
				err := stream.Send(order)
				if err != nil {
					return fmt.Errorf("failed to send order: %v", err)
				}
				log.Print("Sent order" + key)
				break
			}
		}
	}

	return nil
}

func (m *OrderManagement) AddOrder(ctx context.Context, in *pb.Order) (*wrappers.StringValue, error) {
	out, err := uuid.NewV1()
	if err != nil {
		return nil, status.Errorf(codes.Internal, "Error creating UUID: %v", err)
	}

	in.Id = out.String()
	if m.orderMap == nil {
		m.orderMap = make(map[string]*pb.Order)
	}
	m.orderMap[in.Id] = in
	log.Print("Added order " + in.Id)
	return &wrappers.StringValue{Value: in.Id}, status.New(codes.OK, "Order added").Err()
}

func (m *OrderManagement) UpdateOrders(stream pb.OrderManagement_UpdateOrdersServer) error {
	log.Print("Start Update order")
	orderStr := "Updated Order IDs : "
	for {
		order, err := stream.Recv()
		if err == io.EOF {
			return stream.SendAndClose(&wrappers.StringValue{Value: "Orders processed" + orderStr})
		}
		// Update Order
		m.orderMap[order.Id] = order

		log.Print("Updated order " + order.Id)
		orderStr += order.Id + " "
	}

}
