import logging
import re

import grpc
import productinfo_pb2_grpc
from productinfo_pb2 import Product, ProductID


class ProductInfo(productinfo_pb2_grpc.ProductInfoServicer):
    def __init__(self) -> None:
        self.products: dict = {}

    def addProduct(self, request: Product, context) -> ProductID:
        if request.id in self.products.keys():
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("Product already exists")
            return ProductID()
        self.products[request.id] = request

        print(f"I have {len(self.products.keys())} products")
        return ProductID(value=request.id)

    def getProduct(self, request: ProductID, context) -> Product:
        if not request.value in self.products.keys():
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Product not found")
            return Product()
        return self.products[request.value]
