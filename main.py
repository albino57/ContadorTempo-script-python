import registrar_entrada # type: ignore
import registrar_saida #type: ignore
import biblioteca # type: ignore
import backup_simples # type: ignore

#---↑↑ Bibliotecas ↑↑---

#---↓↓ inputs ↓↓---
botao = 'on' #Variável de controle.
#---↑↑ inputs ↑↑---

#---↓↓functions↓↓---
def menu() -> None:
    print('1-Registrar Entrada')
    print('2-Registrar Saída')
    print('3-Criar Backup')
    print('0-Sair')
#---↑↑functions↑↑---

#---↓↓ main  ↓↓---
while True:
    
    try: #Tratamento de erro caso não seja digitado um valor correto.
        if botao == 'on': # Comando que ativa a limpeza de tela apenas pela primeira vez na execução. Isso evita a tela estar suja na primeira execução e evita sempre apagar as mensagens de erro.
            biblioteca.limpar()
            botao = 'off'

        biblioteca.tempo_data()
        print(f'--- Bem-vindo ao Script de tempo de uso no {biblioteca.select_system(biblioteca.system_operation)} ---      Powered by Albino\n') #Comando de impressão na tela.
        menu() #Menu do script
        valor = input('Digite: ') #intereção com o script e conversão para inteiro int()
        selecionar = int(valor)

    except ValueError:
        biblioteca.limpar()
        print(f'\nPor favor, digite uma Opção Válida :) --- Valor digitado: {valor} \n')
        continue
    
    if selecionar not in [0,1,2,3]:
        biblioteca.limpar()
        print('\nDigito inválido!\n')
        continue

    match selecionar: #Funciona como o switch do c++
        case 1:
            biblioteca.limpar()
            registrar_entrada.main()
            continue
        case 2:
            biblioteca.limpar()
            registrar_saida.main()
            continue
        case 3:
            biblioteca.limpar()
            backup_simples.main()
            continue
        case 0:
            print('\n--Script finalizado--')
            #função de tempo de 1,5 segundos.
            break
        case _: #Funciona como o default do c++
            biblioteca.limpar()
            print('\nDigito inválido!\n')
            continue
    biblioteca.limpar()
#---↑↑ main  ↑↑---
#---instruções

#Função	                            Para quê?
#os.path.exists()	                Checar se qualquer caminho existe
#os.path.isdir()	                Checar se é pasta
#os.makedirs(..., exist_ok=True)	Criar pasta, sem erro se já existir
#os.path.isfile()	                Checar se é arquivo
#open('arquivo', 'a')	            Abrir e acrescentar no arquivo
#os.getcwd()	                    Saber diretório de execução
#os.path.join()	                    Montar caminhos de forma segura