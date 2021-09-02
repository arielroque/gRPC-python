# gRPC-python

```bash
virtualenv -p python3 env
source env/bin/activate

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

```