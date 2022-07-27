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

	// TODO: You must remove after testing Deadline
	// time.Sleep(2 * time.Second)

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

func (m *OrderManagement) ProcessOrders(stream pb.OrderManagement_ProcessOrdersServer) error {
	combinedShipmentMap := make(map[string]*pb.CombinedShipment)
	BATCH_SIZE := 3

	for {
		order, err := stream.Recv()
		if err == io.EOF {
			for _, comb := range combinedShipmentMap {
				if len(comb.OrdersList) > 0 {
					stream.Send(comb)
				}
			}
			return nil
		}
		if err != nil {
			return fmt.Errorf("failed to receive order: %v", err)
		}

		out, err := uuid.NewV1()
		if err != nil {
			return fmt.Errorf("error creating UUID: %v", err)
		}
		order.Id = out.String()

		if combinedShipmentMap[order.Destination] == nil {
			orderList := make([]*pb.Order, 0, BATCH_SIZE)
			combinedShipmentMap[order.Destination] = &pb.CombinedShipment{
				Status:      "Processing",
				Destination: order.Destination,
				OrdersList:  orderList,
			}
		}

		combinedShipment := combinedShipmentMap[order.Destination]
		combinedShipment.OrdersList = append(combinedShipment.OrdersList, order)
		log.Printf("Processing order from %v, len: %d", order.Destination, len(combinedShipment.OrdersList))

		if len(combinedShipment.OrdersList) == BATCH_SIZE {
			err := stream.Send(combinedShipmentMap[order.Destination])
			if err != nil {
				return fmt.Errorf("failed to send order: %v", err)
			}
			combinedShipment.OrdersList = make([]*pb.Order, 0, BATCH_SIZE)
		}
	}
}
