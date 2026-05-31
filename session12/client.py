import sys

import grpc

import service_pb2
import service_pb2_grpc


def run(number: int) -> None:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = service_pb2_grpc.CubeServiceStub(channel)
        response = stub.Cube(service_pb2.CubeRequest(number=number))
    print(response.result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: uv run python client.py <number>")

    run(int(sys.argv[1]))
