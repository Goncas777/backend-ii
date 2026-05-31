from concurrent import futures

import grpc

import service_pb2
import service_pb2_grpc


class CubeService(service_pb2_grpc.CubeServiceServicer):
    def Cube(self, request, context):
        result = request.number ** 3
        return service_pb2.CubeReply(result=result)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_CubeServiceServicer_to_server(CubeService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
