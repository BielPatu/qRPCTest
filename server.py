import grpc
import asyncio
import aiofiles
import os
import zipfile
import file_pb2
import file_pb2_grpc

CHUNK_SIZE = 1024 * 64  # 64 KB
FOLDER = "arquivos_enviar"
ZIP_NAME = "FILES_SERVER.zip"
os.makedirs(FOLDER, exist_ok=True)

class FileService(file_pb2_grpc.FileServiceServicer):
    async def GetFile(self, request, context):
        # Sempre cria/atualiza o ZIP com todos os arquivos da pasta
        with zipfile.ZipFile(ZIP_NAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for filename in os.listdir(FOLDER):
                file_path = os.path.join(FOLDER, filename)
                if os.path.isfile(file_path):
                    zipf.write(file_path, arcname=filename)

        # Abre o ZIP e envia em chunks
        async with aiofiles.open(ZIP_NAME, "rb") as f:
            while chunk := await f.read(CHUNK_SIZE):
                yield file_pb2.FileChunk(data=chunk)

async def serve():
    server = grpc.aio.server()
    file_pb2_grpc.add_FileServiceServicer_to_server(FileService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    print("Servidor rodando na porta 50051...")
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())