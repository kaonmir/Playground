

### Python으로 gRPC 스켈레톤 코드를 생성한다.

`python3 -m grpc_tools.protoc -I ecommerce --python_out=.  --grpc_python_out=.  ecommerce/productinfo.proto `