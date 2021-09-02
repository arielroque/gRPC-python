import grpc
from calculator import timestamp

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = calculator_pb2.Number(value=16)
emptyRequest = calculator_pb2.EmptyRequest()

# make the call
response = stub.SquareRoot(number)

print(response.value)

response = stub.Timestamp(emptyRequest)

print(response.value)