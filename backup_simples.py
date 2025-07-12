import os
import zipfile
import biblioteca
import datetime
#---↑↑Bibliotecas↑↑---

def main():
    if(os.name == 'posix'): #Se for Sistema Linux "posix"
        diretorio_origem = 'dados'
        diretorio_destino = f'backups/backup_20{str(biblioteca.v_ano())}'
        data_hora = datetime.datetime.now().strftime('%Y.%m.%d__%H.%M.%S')
        os.makedirs(diretorio_destino, exist_ok=True)

        nome_arquivo = f'backup_{data_hora}.zip'
        caminho_backup = os.path.join(diretorio_destino, nome_arquivo) # os.path.join torna o endereço compatível com Windows/Linux.

        with zipfile.ZipFile(caminho_backup, 'w', zipfile.ZIP_DEFLATED) as zipf: # w é modo de escrita/cria | ZIP_DEFLATED aplica compressão nos arquivos.
            for raiz, dirs, arquivos in os.walk(diretorio_origem): #os.walk() vai percorrer todas as subpastas e arquivos.
                for arquivo in arquivos:
                    caminho_completo = os.path.join(raiz, arquivo) # os.path.join torna o endereço compatível com Windows/Linux.
                    caminho_relativo = os.path.relpath(caminho_completo, diretorio_origem) # os.path.relpath torna o endereço de backup menor removendo o diretorio_origem
                    zipf.write(caminho_completo, arcname=caminho_relativo) # arcname= garante que a estrutura dentro do zip fique limpa e organizada.

    if(os.name == 'nt'): #Se for Sistema Windows "nt"
        diretorio_origem = 'dados'
        diretorio_destino = f'backups\\backup_20{str(biblioteca.v_ano())}'
        data_hora = datetime.datetime.now().strftime('%Y.%m.%d__%H.%M.%S')
        os.makedirs(diretorio_destino, exist_ok=True)

        nome_arquivo = f'backup_{data_hora}.zip'
        caminho_backup = os.path.join(diretorio_destino, nome_arquivo) # os.path.join torna o endereço compatível com Windows/Linux.

        with zipfile.ZipFile(caminho_backup, 'w', zipfile.ZIP_DEFLATED) as zipf: # w é modo de escrita/cria | ZIP_DEFLATED aplica compressão nos arquivos.
            for raiz, dirs, arquivos in os.walk(diretorio_origem): #os.walk() vai percorrer todas as subpastas e arquivos.
                for arquivo in arquivos:
                    caminho_completo = os.path.join(raiz, arquivo) # os.path.join torna o endereço compatível com Windows/Linux.
                    caminho_relativo = os.path.relpath(caminho_completo, diretorio_origem) # os.path.relpath torna o endereço de backup menor removendo o diretorio_origem
                    zipf.write(caminho_completo, arcname=caminho_relativo) # arcname= garante que a estrutura dentro do zip fique limpa e organizada.

    print(f'\n📦 Backup criado com sucesso: {caminho_backup}\n')
    
if __name__ == '__main__':
    main()