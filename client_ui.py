import grpc
import file_pb2
import file_pb2_grpc
import tkinter as tk
from tkinter import messagebox
import threading
import os
import aiofiles
import asyncio

SERVER_ADDRESS = "26.190.20.9:50051"
RECEIVE_FOLDER = "arquivos_recebidos"
filename = "FILES_SERVER.zip"

def receive_file():
    async def task():
        try:
            async with grpc.aio.insecure_channel(SERVER_ADDRESS) as channel:
                stub = file_pb2_grpc.FileServiceStub(channel)

                response = stub.GetFile(file_pb2.FileRequest(file_name=filename))

                os.makedirs(RECEIVE_FOLDER, exist_ok=True)
                output_path = os.path.join(RECEIVE_FOLDER, filename)

                async with aiofiles.open(output_path, "wb") as f:
                    print(f"Iniciando download de {filename}...")
                    async for chunk in response:
                        await f.write(chunk.data)

            root.after(0, lambda: messagebox.showinfo(
                "Sucesso", "Arquivos recebidos com sucesso!"
            ))

        except Exception as e:
            root.after(0, lambda: messagebox.showerror("Erro", str(e)))

    # Cria uma thread que roda o loop de eventos async
    threading.Thread(target=lambda: asyncio.run(task()), daemon=True).start()


# --- UI ---
root = tk.Tk()
root.title("Cliente gRPC")

tk.Label(root, text="Clique para receber o arquivo do servidor").pack(pady=10)
tk.Button(root, text="Receber Arquivo", command=receive_file).pack(pady=10)

root.mainloop()