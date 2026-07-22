from dao import conectar

try:
    conexao = conectar()

    print("Conectado com sucesso!")

    conexao.close()

except Exception as erro:

    print(erro)