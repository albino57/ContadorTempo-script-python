import os #biblioteca operating system
import csv #biblioteca de manipulação de arquivos csv
import biblioteca # type: ignore
#---↑↑Bibliotecas↑↑---

#---↓↓Variáveis_Globais↓↓---
val_meses = biblioteca.fun_meses()
#---↑↑Variáveis_Globais↑↑---

#---↓↓funções↓↓---
def main() -> None:
    os.makedirs('dados', exist_ok=True) #Verifica/Cria a pasta principal de dados.

#↓↓IF do Linux↓↓============================================================================================================================================================================================
    if(os.name == 'posix'): #Se for Sistema Linux "posix"
        
        if (os.path.isdir('dados/20' + str(biblioteca.v_ano()) + '/' + '0' + str(biblioteca.v_mes()) + '-' + val_meses[biblioteca.v_mes()-1])) or (os.path.isdir('dados/20' + str(biblioteca.v_ano()) + '/' + str(biblioteca.v_mes()) + '-' + val_meses[biblioteca.v_mes()-1])) == False: #Verifica se o diretório existe, se não Cria.
            os.makedirs('dados/20' + str(biblioteca.v_ano()) + '/' + str(biblioteca.v_mes()) + '-' + val_meses[int(biblioteca.v_mes())-1], exist_ok=True) #Cria o diretório
            print('\n>Diretório', '"dados/20' + str(biblioteca.v_ano()) + '/' + str(biblioteca.v_mes()) + '-' + val_meses[int(biblioteca.v_mes())-1] + '"', 'foi criado!') #imprime uma mensagem de confirmação.

        diretorio = f'dados/20{biblioteca.v_ano()}/{biblioteca.v_mes()}-{val_meses[biblioteca.v_mes()-1]}/dia_{str(biblioteca.v_dia())}.csv' #Obtem o endereço dinâmico para cada executação ou dia/Mês/Ano
        os.makedirs(os.path.dirname(diretorio), exist_ok=True) #Confirma de o diretório existe.

        #
        if os.path.isfile(diretorio) == True: #Verifica se o Arquivo existe, se sim. É verificado abaixo se existe uma Entrada.
            with open(diretorio, mode='r', encoding='utf-8') as arquivo_csv:
                ultima_linha = None

                for linha in csv.reader(arquivo_csv): #Esse for acha a última linha do arquivo.
                    if linha != []:
                       ultima_linha = linha

                if ultima_linha and ultima_linha[0].strip().lower() == 'entrada': #strip() remove o \n e lower transforma a palavra em minuscula.
                    print(f'\n > Já existe entrada no arquivo dia_{str(biblioteca.v_dia())} no diretório dados/20{biblioteca.v_ano()}/{biblioteca.v_mes()}-{val_meses[biblioteca.v_mes()-1]} <')
                    print(f'   Última Linha: {ultima_linha}\n')
            
                else:
                    with open(diretorio, mode='a', newline='', encoding='utf-8') as arquivo_csv: #Abre o Arquivo
                        escritor = csv.writer(arquivo_csv) #escritor recebe algo que ainda não sei
                        escritor.writerow([f'Entrada', str(biblioteca.v_data()), str(biblioteca.v_horario())])
                        print(f'\n > Arquivo dia_{str(biblioteca.v_dia())}.cvs Atualizado!')
                
                    print(f'   {biblioteca.buscar_ultima_linha(diretorio)}\n')
        
        # If de rastreamento
        if not os.path.isfile(diretorio): #Verifica se o arquivo existe, se não, busca se existe algum antes
        
            biblioteca.rastrear_entradasaida('sem Saída')

        #If de Criação do Arquivo e Configuração.
        if os.path.isfile(diretorio) != True: #Verifica se o Arquivo existe, se não. É criado e configurado.
            with open(diretorio, mode='a', newline='', encoding='utf-8') as arquivo_csv: #Cria/Abre o Arquivo
                escritor = csv.writer(arquivo_csv) #escritor recebe algo que ainda não sei

                if arquivo_csv.tell() == 0: # Checa se o aquivo está vazio e se TRUE, cria o carimbo do arquivo.
                    escritor.writerow([f'{biblioteca.v_data()} - {biblioteca.v_horario()} GMT-3']) #Escreve no arquivo.
                    escritor.writerow([]) # Pula linha

                    escritor.writerow(['TipoDeEntrada','Data','Hora'])
                    escritor.writerow([]) # Pula linha
                    print(f'\n >Arquivo dia_{str(biblioteca.v_dia())}.cvs foi criado!')

                if arquivo_csv.tell() != 0: #Verifica se o arquivo tem alguma informação e se sim, entra com o registro de entrada.
                    escritor.writerow([f'Entrada', str(biblioteca.v_data()), str(biblioteca.v_horario())])
                    print(f'\n >Arquivo dia_{str(biblioteca.v_dia())}.cvs Atualizado!\n')
                    print(f' {biblioteca.buscar_ultima_linha(diretorio)}')
#↑↑IF do Linux↑↑============================================================================================================================================================================================

#↓↓IF do Windows↓↓============================================================================================================================================================================================   
    if(os.name == 'nt'): #Se for Sistema Windows "nt"

        if (os.path.isdir('dados\\20' + str(biblioteca.v_ano()) + '\\' + '0' + str(biblioteca.v_mes()) + '-' + val_meses[biblioteca.v_mes()-1])) or (os.path.isdir('dados\\20' + str(biblioteca.v_ano()) + '\\' + str(biblioteca.v_mes()) + '-' + val_meses[biblioteca.v_mes()-1])) == False: #Verifica se o diretório existe, se não Cria.
            os.makedirs('dados\\20' + str(biblioteca.v_ano()) + '\\' + str(biblioteca.v_mes()) + '-' + val_meses[int(biblioteca.v_mes())-1], exist_ok=True) #Cria o diretório
            print('\n>Diretório', '"dados\\20' + str(biblioteca.v_ano()) + '\\' + str(biblioteca.v_mes()) + '-' + val_meses[int(biblioteca.v_mes())-1] + '"', 'foi criado!') #imprime uma mensagem de confirmação.

        diretorio = f'dados\\20{biblioteca.v_ano()}\\{biblioteca.v_mes()}-{val_meses[biblioteca.v_mes()-1]}\\dia_{str(biblioteca.v_dia())}.csv' #Obtem o endereço dinâmico para cada executação ou dia/Mês/Ano
        os.makedirs(os.path.dirname(diretorio), exist_ok=True) #Confirma de o diretório existe.

        #
        if os.path.isfile(diretorio) == True: #Verifica se o Arquivo existe, se sim. É verificado abaixo se existe uma Entrada.
            with open(diretorio, mode='r', encoding='utf-8') as arquivo_csv:
                ultima_linha = None

                for linha in csv.reader(arquivo_csv): #Esse for acha a última linha do arquivo.
                    if linha != []:
                       ultima_linha = linha

                if ultima_linha and ultima_linha[0].strip().lower() == 'entrada': #strip() remove o \n e lower transforma a palavra em minuscula.
                    print(f'\n > Já existe entrada no arquivo dia_{str(biblioteca.v_dia())} no diretório dados\\20{biblioteca.v_ano()}\\{biblioteca.v_mes()}-{val_meses[biblioteca.v_mes()-1]} <')
                    print(f'   Última Linha: {ultima_linha}\n')
            
                else:
                    with open(diretorio, mode='a', newline='', encoding='utf-8') as arquivo_csv: #Abre o Arquivo
                        escritor = csv.writer(arquivo_csv) #escritor recebe algo que ainda não sei
                        escritor.writerow([f'Entrada', str(biblioteca.v_data()), str(biblioteca.v_horario())])
                        print(f'\n > Arquivo dia_{str(biblioteca.v_dia())}.cvs Atualizado!')
                
                    print(f'   {biblioteca.buscar_ultima_linha(diretorio)}\n')
                
        # If de rastreamento
        if not os.path.isfile(diretorio): #Verifica se o arquivo existe, se não, busca se existe algum antes
        
            biblioteca.rastrear_entradasaida('sem Saída')

        #If de Criação do Arquivo e Configuração.
        if os.path.isfile(diretorio) != True: #Verifica se o Arquivo existe, se não. É criado e configurado.
            with open(diretorio, mode='a', newline='', encoding='utf-8') as arquivo_csv: #Cria/Abre o Arquivo
                escritor = csv.writer(arquivo_csv) #escritor recebe algo que ainda não sei

                if arquivo_csv.tell() == 0: # Checa se o aquivo está vazio e se TRUE, cria o carimbo do arquivo.
                    escritor.writerow([f'{biblioteca.v_data()} - {biblioteca.v_horario()} GMT-3']) #Escreve no arquivo.
                    escritor.writerow([]) # Pula linha

                    escritor.writerow(['TipoDeEntrada','Data','Hora'])
                    escritor.writerow([]) # Pula linha
                    print(f'\n >Arquivo dia_{str(biblioteca.v_dia())}.cvs foi criado!')

                if arquivo_csv.tell() != 0: #Verifica se o arquivo tem alguma informação e se sim, entra com o registro de entrada.
                    escritor.writerow([f'Entrada', str(biblioteca.v_data()), str(biblioteca.v_horario())])
                    print(f'\n >Arquivo dia_{str(biblioteca.v_dia())}.cvs Atualizado!\n')
                    print(f' {biblioteca.buscar_ultima_linha(diretorio)}')
#↑↑IF do Windows↑↑=========================================================================================================================================================================================   
#---↑↑funções↑↑---

#---↓↓main↓↓---
if __name__ == '__main__':
    main() #chama e executa o script caso o script principal de chamada esteja danificado/corrompido ou para testes.
#---↑↑main↑↑---