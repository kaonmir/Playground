package main

import (
	"context"
	"flag"
	"log"
	"net"
	pb "productinfo/protos"

	"github.com/gofrs/uuid"
	"github.com/golang/protobuf/ptypes/wrappers"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

type server struct {
	pb.UnimplementedProductInfoServer
	pb.UnimplementedOrderManagementServer
	productMap map[string]*pb.Product
	orderMap   map[string]*pb.Order
}

func (s *server) AddProduct(ctx context.Context, in *pb.Product) (*pb.ProductID, error) {
	out, err := uuid.NewV4()
	if err != nil {
		return nil, status.Errorf(codes.Internal, "Error creating UUID: %v", err)
	}

	in.Id = out.String()
	if s.productMap[in.Id] == nil {
		s.productMap = make(map[string]*pb.Product)
	}
	s.productMap[in.Id] = in
	return &pb.ProductID{Value: in.Id}, status.New(codes.OK, "Product added").Err()
}

func (s *server) GetProduct(ctx context.Context, in *pb.ProductID) (*pb.Product, error) {
	value, exists := s.productMap[in.Value]
	if exists {
		return value, status.New(codes.OK, "Product found").Err()
	}
	return nil, status.Errorf(codes.NotFound, "Product not found", in.Value)
}

func (s *server) GetOrder(ctx context.Context, in *wrappers.StringValue) (*pb.Order, error) {
	if s.orderMap[in.Value] == nil {
		return nil, status.Errorf(codes.NotFound, "Order not found", in.Value)
	}

	ord := s.orderMap[in.Value]
	return ord, status.New(codes.OK, "Order found").Err()
}

var (
	addr = flag.String("addr", "localhost:50051", "the address to connect to")
)

func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", *addr)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterProductInfoServer(s, &server{})
	pb.RegisterOrderManagementServer(s, &server{})

	log.Printf("Server listening on %s", *addr)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
