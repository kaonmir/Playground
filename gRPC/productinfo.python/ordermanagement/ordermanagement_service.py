import logging
import re

import grpc
import ordermanagement_pb2_grpc as pb2_grpc
import ordermanagement_pb2 as pb2

from google.protobuf import wrappers_pb2


class ProductInfo(pb2_grpc.OrderManagementServicer):
    def __init__(self):
        self.orderMap: list = [
            pb2.Order(
                id=1,
                items=[1, 2, 3],
                price=100,
                destination="India",
                description="Order 1",
            ),
        ]

    def GetOrder(self, orderId: wrappers_pb2.StringValue, context) -> pb2.Order:
        ord = self.orderMap[orderId.value]
        return ord

    ...
