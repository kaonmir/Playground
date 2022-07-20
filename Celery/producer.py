import sys
import pika

queue = "son_queue"
message = " ".join(sys.argv[1:])

# Connection 생성
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="192.168.25.40",
        port=5672,
        virtual_host="/",
        credentials=pika.PlainCredentials("son", "son"),  # username, password
    )
)

# Server와 통신하기 위한 channel 생성
channel = connection.channel()

# Message Queue 생성
channel.queue_declare(queue=queue)

# Message 전송
channel.basic_publish(
    exchange="",  # 다른 Queue로 Routing하는 역할
    routing_key=queue,  # Message를 적재할 Queue
    body=message,  # 전송할 Message
)
print(" [x] Sent " + message)

# Connection 종료
connection.close()
