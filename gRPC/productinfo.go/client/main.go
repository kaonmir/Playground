package main

import (
	"flag"
	"log"
)

var (
	addr    = flag.String("addr", "localhost:50051", "the address to connect to")
	senario = flag.String("senario", "1", "the senario to run")
)

func main() {
	flag.Parse()
	conn, ctx, cancel, c := NewOrderManagementClient()
	defer conn.Close()
	defer cancel()

	log.Print("Running Senario ", *senario)

	switch ch := *senario; ch {
	case "1":
		Senario1(ctx, c)
	case "2":
		Senario2(ctx, c)
	case "3":
		Senario3(ctx, c)
	}
}
