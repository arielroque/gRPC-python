import grpc

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
square_root = stub.SquareRoot(number)
timestamp = stub.Timestamp(emptyRequest)

print(square_root.value)
print(timestamp.value)