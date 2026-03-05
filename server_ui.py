import tkinter as tk
from server import serve
import threading
from tkinter import ttk, messagebox
import asyncio
import aiofiles

server_instance = None

def start_server():
    global server_instance
    def run_server():
        global server_instance
        server_instance = asyncio.run(serve())
        server_instance.wait_for_termination()  # Mantém o servidor rodando
    threading.Thread(target=run_server, daemon=True).start()
    status_label.config(text="Servidor rodando na porta 50051")

def stop_server():
    global server_instance
    if server_instance:
        server_instance.stop(0)
        status_label.config(text="Servidor parado")
        server_instance = None

root = tk.Tk()
root.title("Servidor de Arquivos")

tk.Button(root, text="Iniciar Servidor", command=start_server).pack(pady=10)
tk.Button(root, text="Parar Servidor", command=stop_server).pack(pady=10)

status_label = tk.Label(root, text="Servidor parado")
status_label = tk.Label(root, text="Tamanho Do Arquivo")
status_label.pack(pady=10)

progress = ttk.Progressbar(root, length=300, mode="determinate")
progress.pack(pady=10)

root.mainloop()