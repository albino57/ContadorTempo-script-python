import os #biblioteca operating system
import datetime #biblioteca de tempo :D
import biblioteca # type: ignore
import csv #biblioteca de manipulação de arquivos csv

#---↓↓ inputs ↓↓---
system_operation = os.name #Salva qual OS está sendo usado.

#---↑↑ inputs ↑↑---

#---↓↓functions↓↓---
def fun_meses() -> str:
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    return meses

def barras() -> str:
    if(os.name == 'posix'):
        barra = '/'
        return barra
    if(os.name == 'nt'):
        barra = '\\'

def buscar_ultima_linha(diretorio) -> str:
    diretorio_corrigido = diretorio
    if os.path.isfile(diretorio_corrigido):
        with open(diretorio_corrigido, mode='r', encoding='utf-8') as arquivo_csv:
            ultima_linha = None
            for linha in csv.reader(arquivo_csv): #Esse for acha a última linha do arquivo.
                if linha != []:
                    ultima_linha = linha
        return ultima_linha

def rastrear_entradasaida(parametro) -> None:
    mensagem = parametro
    for w in range(int(biblioteca.v_ano()),0,-1): # for primario de busca [Categoria: ANO] --- range(início, fim, passo)
        if not os.path.isdir(f'dados{barras()}20{w}'): return #Verifica se o diretório existe, se não. para a executação da função.
        
        for i in range(12,0,-1):  # range(início, fim, passo)
            for x in range(31,0,-1):
                diretorio_correcao = f'dados{barras()}20{w}{barras()}{i}-{fun_meses()[i-1]}{barras()}dia_{x}.csv'

                if os.path.isfile(diretorio_correcao):
                    with open(diretorio_correcao, mode='r', encoding='utf-8') as arquivo_csv:
                        penultima_linha = None
                        ultima_linha = None
                        
                        for linha in csv.reader(arquivo_csv): #Esse for acha a última linha do arquivo.
                            if linha != []:
                                penultima_linha = ultima_linha
                                ultima_linha = linha

                    if ultima_linha and ultima_linha[0].strip().lower() == 'entrada':
                        print(f' > Foi encontrado um arquivo {diretorio_correcao}, {mensagem}.')
                        with open(diretorio_correcao, mode='a', newline='', encoding='utf-8') as arquivo_csv: #Abre o Arquivo para editar.
                            escritor = csv.writer(arquivo_csv) #
                            escritor.writerow([f'Saída', '  '+str(biblioteca.v_data()), str(biblioteca.v_horario())]) #Inseri a Saída

                        print(f'   Últimas Linhas: {penultima_linha}')
                        print(f'                   {ultima_linha}\n')
                        print(' > Saída adicionada com sucesso.')
                        print(f'                   {buscar_ultima_linha(diretorio_correcao)}')
                        return #Encerra o processamento da função.

def select_system(system_operation: str) -> str: #Uma função em python.
    if system_operation == 'nt':
        return 'Windows'
    elif system_operation == 'posix': #elif funciona como o if else em c++
        return 'Linux' 

def tempo_data() -> None: #Função de impressão de tempo.
    tempo = datetime.datetime.now() #Carrega na variável o valor atual do tempo.
    print ('-*'*28, tempo.date(), '-', tempo.strftime('%H:%M:%S'))

def limpar() -> None:
    os.system('cls' if os.name == 'nt' else 'clear') #Usa cls no Windows e clear no Linux/Mac e os.name retorna 'nt' no Windows e 'posix' no Linux/Mac
    #os.system(): Executa o comando do sistema operacional

def v_data() -> int:
    data = datetime.datetime.now()
    return data.date()

def v_horario() -> int:
    data = datetime.datetime.now()
    return data.strftime('%H:%M:%S')

def v_ano() -> int:
    data = datetime.datetime.now()
    ano = int(data.strftime('%y'))
    return ano

def v_mes() -> int:
    data = datetime.datetime.now()
    mes = int(data.strftime('%m'))
    return mes

def v_dia() -> int:
    data = datetime.datetime.now()
    dia = int(data.strftime('%d'))
    return dia

def v_hora() -> int:
    data = datetime.datetime.now()  
    hora = int(data.strftime('%H'))
    return hora

def v_minuto() -> int:     
    data = datetime.datetime.now()
    minuto = int(data.strftime('%M'))
    return minuto

def v_segundo() -> int:
    data = datetime.datetime.now()
    segundo = int(data.strftime('%S'))
    return segundo