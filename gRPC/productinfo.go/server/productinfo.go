package main

import (
	"context"
	pb "productinfo/protos"

	"github.com/gofrs/uuid"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

type ProductInfo struct {
	pb.UnimplementedProductInfoServer
	productMap map[string]*pb.Product
}

func (p *ProductInfo) AddProduct(ctx context.Context, in *pb.Product) (*pb.ProductID, error) {
	out, err := uuid.NewV4()
	if err != nil {
		return nil, status.Errorf(codes.Internal, "Error creating UUID: %v", err)
	}

	in.Id = out.String()
	if p.productMap[in.Id] == nil {
		p.productMap = make(map[string]*pb.Product)
	}
	p.productMap[in.Id] = in
	return &pb.ProductID{Value: in.Id}, status.New(codes.OK, "Product added").Err()
}

func (p *ProductInfo) GetProduct(ctx context.Context, in *pb.ProductID) (*pb.Product, error) {
	value, exists := p.productMap[in.Value]
	if exists {
		return value, status.New(codes.OK, "Product found").Err()
	}
	return nil, status.Errorf(codes.NotFound, "Product not found", in.Value)
}
