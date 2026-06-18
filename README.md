# qRPCTest

Projeto de exemplo para transferências de arquivos usando gRPC em Python.

## Descrição

Este projeto implementa um servidor e um cliente para envio/recebimento de arquivos usando gRPC. Há implementações tanto em linha de comando quanto com interfaces gráficas simples (UI).

Principais funcionalidades:
- Enviar arquivos do cliente para o servidor via gRPC
- Receber e salvar arquivos no servidor
- Interfaces CLI e UI para servidor e cliente

## Requisitos

- Python 3.8+ (testado em 3.8/3.9/3.10)
- Dependências: `grpcio`, `grpcio-tools` (opcional se os arquivos gerados já estiverem presentes)

Exemplo de instalação rápida das dependências:

```powershell
python -m pip install grpcio grpcio-tools
```

Se preferir, crie um `requirements.txt` com as dependências acima.

## Estrutura do projeto

- `file.proto` - definição do serviço e mensagens gRPC
- `file_pb2.py`, `file_pb2_grpc.py` - código gerado a partir do `.proto` (já versionado neste repositório)
- `server.py` - servidor gRPC (backend)
- `client.py` - cliente para envio de arquivos (CLI)
- `server_ui.py` - interface gráfica para o servidor
- `client_ui.py` - interface gráfica para o cliente
- `arquivos_enviar/` - pasta sugerida para colocar arquivos que serão enviados
- `arquivos_recebidos/` - pasta onde o servidor salva arquivos recebidos

## Gerar/Atualizar arquivos gRPC (opcional)

Se você modificar `file.proto`, regenere os arquivos Python com:

```powershell
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. file.proto
```

Isso produzirá/atualizará `file_pb2.py` e `file_pb2_grpc.py`.

## Uso

1) Rodar o servidor (CLI):

```powershell
python server.py
```

2) Rodar o cliente (CLI) para enviar um arquivo:

```powershell
python client.py caminho/para/arquivo.ext
```

3) Executar as UIs (se desejar interfaces gráficas):

```powershell
python server_ui.py
python client_ui.py
```

Observação: os argumentos exatos da linha de comando dependem da implementação atual de `server.py` e `client.py`. Se necessário, abra os arquivos para checar opções e parâmetros.

## Boas práticas

- Coloque arquivos a enviar em `arquivos_enviar/` para testes rápidos.
- Verifique as permissões de escrita em `arquivos_recebidos/` no servidor.

## Contribuição

Sugestões e correções são bem-vindas. Abra issues ou pull requests com melhorias.

## Contato

Mantenha o desenvolvedor informado sobre bugs ou dúvidas.

---
Gerado automaticamente: documentação básica adicionada para facilitar testes e uso local.
