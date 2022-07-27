package main

import (
	"flag"
	"log"
	"net"
	pb "productinfo/protos"

	"productinfo/server/interceptor"

	"google.golang.org/grpc"
)

var (
	addr = flag.String("addr", "localhost:50051", "the address to connect to")
)

func main() {
	flag.Parse()

	lis, err := net.Listen("tcp", *addr)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer(
		grpc.UnaryInterceptor(interceptor.OrderUnaryServerInterceptor),
		grpc.StreamInterceptor(interceptor.OrderServerStreamInterceptor),
	)
	pb.RegisterProductInfoServer(s, &ProductInfo{})
	pb.RegisterOrderManagementServer(s, &OrderManagement{})

	log.Printf("Server listening on %s", *addr)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
