from concurrent import futures
import logging
import grpc
from productinfo_service import ProductInfo
from productinfo_pb2_grpc import add_ProductInfoServicer_to_server


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ProductInfoServicer_to_server(ProductInfo(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
