package interceptor

import (
	"log"
	"time"

	"google.golang.org/grpc"
)

// Stream은 전처리 -> 스트림 -> 후처리 순으로 진행된다.

type WrappedStream struct {
	grpc.ServerStream
}

func (w *WrappedStream) RecvMsg(m interface{}) error {
	log.Printf("===== [Server Stream Interceptor Wrapper] "+
		"Receive a message (Type: %T) at %v",
		m, time.Now().Format(time.RFC1123))
	return w.ServerStream.RecvMsg(m)
}

func (w *WrappedStream) SendMsg(m interface{}) error {
	log.Printf("===== [Server Stream Interceptor Wrapper] "+
		"Send a message (Type: %T) at %v",
		m, time.Now().Format(time.RFC1123))
	return w.ServerStream.SendMsg(m)
}

func newWrappedStream(s grpc.ServerStream) grpc.ServerStream {
	return &WrappedStream{s}
}

func OrderServerStreamInterceptor(
	srv interface{}, ss grpc.ServerStream, info *grpc.StreamServerInfo, handler grpc.StreamHandler) error {
	log.Println("===== [Server Stream Interceptor] ", info.FullMethod)
	err := handler(srv, newWrappedStream(ss))
	if err != nil {
		log.Printf("RPC failed: %v", err)
	}
	return err

}
