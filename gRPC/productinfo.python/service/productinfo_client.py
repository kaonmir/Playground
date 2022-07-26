from __future__ import print_function

import logging

import grpc
import productinfo_pb2
import productinfo_pb2_grpc


def run():
    try:
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = productinfo_pb2_grpc.ProductInfoStub(channel)
            response = stub.addProduct(
                productinfo_pb2.Product(id="wednesday", name="wow")
            )
        print("Response: ", response)
    except grpc.RpcError as e:
        print(e.code())
        print(e.details())

    # get response status code


if __name__ == "__main__":
    logging.basicConfig()
    run()
