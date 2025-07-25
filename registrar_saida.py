import os #biblioteca operating system
import csv #biblioteca de manipulação de arquivos csv
import biblioteca # type: ignore
#---↑↑Bibliotecas↑↑---

#---↓↓Variáveis_Globais↓↓---
val_meses = biblioteca.fun_meses()
#---↑↑Variáveis_Globais↑↑---

#---↓↓funções↓↓---
def barras() -> str:
    if(os.name == 'posix'):
        barra = '/'
        return barra
    if(os.name == 'nt'):
        barra = '\\'
        
def main():

    #Variáveis para melhorar visibilidade do código.
    ano = biblioteca.v_ano()
    mes = biblioteca.v_mes()
    dia = biblioteca.v_dia()
    mes_nome = val_meses[mes -1]
    dir_normal = f'dados{barras()}20{ano}{barras()}{mes}-{mes_nome}'

    diretorio = f'{dir_normal}{barras()}dia_{dia}.csv' #Obtem o endereço dinâmico para cada executação ou dia/Mês/Ano
    
    if os.path.isfile(diretorio):
        with open(diretorio, mode='a', newline='', encoding='utf-8') as arquivo_csv: #Cria/Abre o Arquivo
            escritor = csv.writer(arquivo_csv) #escritor recebe algo que ainda não sei

            if arquivo_csv.tell() == 0: # Checa se o aquivo está vazio e se TRUE, cria o carimbo do arquivo.
                print(f'\n>Arquivo dia_{dia}.cvs está vazio, execute o Script "registrar_entrada.py" para criar o cabeçalho e a entrada para proseguir. ')

            if arquivo_csv.tell() != 0: #Verifica se o arquivo tem alguma informação e se sim, entra com o registro de saída.
                escritor.writerow([f'Saída', '  '+str(biblioteca.v_data()), str(biblioteca.v_horario())]) #Inseri a Saída
                print(f'\n > Arquivo dia_{dia}.cvs Atualizado!')
                
    else:
        print(f'\n>Arquivo dia_{dia}.cvs não existe!\n')

    print(f'   {biblioteca.buscar_ultima_linha(diretorio)}\n')# Imprimi a saída para conferência visual.

    if not os.path.isfile(diretorio):
        biblioteca.rastrear_entradasaida('com Entrada')

#---↑↑funções↑↑---

#---↓↓main↓↓---
if __name__ == '__main__':
    main() #chama e executa o script caso o script principal de chamada esteja danificado/corrompido ou para testes.
#---↑↑main↑↑---