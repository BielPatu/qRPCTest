import grpc
import asyncio
import aiofiles
import file_pb2
import file_pb2_grpc
import os

RECEIVE_FOLDER = "arquivos_recebidos"
filename = "FILES_SERVER.zip"

async def run():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = file_pb2_grpc.FileServiceStub(channel)
        response_iterator = stub.GetFile(file_pb2.FileRequest(file_name=filename))

        os.makedirs(RECEIVE_FOLDER, exist_ok=True)
        output_path = os.path.join(RECEIVE_FOLDER, filename)

        async with aiofiles.open(output_path, "wb") as f:
            print(f"Iniciando download de {filename}...")
            async for chunk in response_iterator:
                await f.write(chunk.data)

        print("Download completo!")

if __name__ == "__main__":
    asyncio.run(run())