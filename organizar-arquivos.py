import os
import shutil
from datetime import datetime

#função para criar uma pasta se ela não existir
def criar_pasta(caminho):
    if not os.path.exists(caminho):
        os.makedirs(caminho)

#função para organizar os arquivos
def organizar_arquivos(pasta_origem, pasta_destino):
    #lista todos os arquivos na pasta de origem
    for arquivo in os.listdir(pasta_origem):
        caminho_completo = os.path.join(pasta_origem, arquivo)
        
        #ignora pastas (so organiza arquivos)
        if os.path.isdir(caminho_completo):
            continue
        
        #pega a extensão do arquivo... ex: .txt, .jpg
        extensao = os.path.splitext(arquivo)[1].lower()
        
        #define a pasta de destino baseada na extensão
        if extensao:
            pasta_extensao = os.path.join(pasta_destino, extensao[1:])  # Remove o ponto da extensão
        else:
            pasta_extensao = os.path.join(pasta_destino, "outros")  # Para arquivos sem extensão
        
        #cria a pasta se não existir
        criar_pasta(pasta_extensao)
        
        #gera um novo nome para o arquivo com a data e hora
        data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        novo_nome = f"{data_hora}_{arquivo}"
        
        #move o arquivo para a pasta de destino com o novo nome
        shutil.move(caminho_completo, os.path.join(pasta_extensao, novo_nome))

#parte principal do programa
if __name__ == "__main__":
    #define as pastas de origem e destino
    pasta_origem = r"C:\Users\ingri\Downloads"
    pasta_destino = r"c:\Users\ingri\Downloads\Documentos\IMPORTANTE"
    
    #organiza os arquivos
    organizar_arquivos(pasta_origem, pasta_destino)
    print("Arquivos organizados com sucesso!")