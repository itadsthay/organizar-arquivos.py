"""Organizador de Arquivos Automático"""

Este é um script Python que organiza arquivos em pastas baseadas em suas extensões e renomeia os arquivos com um timestamp para evitar conflitos de nomes.

"""Como usar"""

1. Baixe o script `organizar-arquivos.py`.
2. Modifique as variáveis `diretorio_origem` e `diretorio_destino` no script para apontar para os diretórios desejados.
3. Execute o script usando Python:
   ```bash
   python organizar-arquivos.py
#------------------------------
"""Funcionalidades"""
Organiza arquivos por extensão, e cria uma pasta para cada arquivo dentro da pasta principal (ex: .txt vai para a pasta txt).
Renomeia arquivos com a data e hora atual (ex: 20231025_143022_foto.jpg).
Arquivos sem extensão são movidos para a pasta outros.