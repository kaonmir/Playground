package interceptor

import (
	"context"
	"log"

	"google.golang.org/grpc"
)

func OrderUnaryServerInterceptor(
	ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {

	log.Println("===== [Server Interceptor] ", info.FullMethod)

	m, err := handler(ctx, req)
	log.Print("Post Proc Message : ", m)
	return m, err
}
