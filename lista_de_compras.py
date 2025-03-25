

lista = [ 'Manteiga', 'Leite', 'Óleo']



def Verficar_opcoes():
    print('Menu lista de compras: ')

    print('Opção 1 - LER, Opção 2- REMOVER, Opção 3 - ADCIONAR, Opção 0 - Sair')
    opcao = int(input('Digite o opção: '))

    match opcao:
        case 1: 
            Ler()
        case 2:
            Apagar()
        case 3: 
            Adicionar()
        case 0:
            print('Até mais...')
            
    

def Ler():
    print('LISTANDO INTENS:')
    numerar = 0
    for item in lista:
        numerar += 1
        print(f'{numerar} - {item}')
    input('\nPressione enter para voltar...\n')
    Verficar_opcoes()
    
      

def Apagar ():
    print('APAGAR NUMEROS: ')
    numero = int(input('\nDigite o numero do item que quer apagar: '))
    if numero > 0: 
        numero += 1
        lista.pop(numero)
        print (f'Número {numero} removido!')
    else: 
        print('Não possui item nesse indíce ')
    input('\nPressione enter para voltar...\n')
    Verficar_opcoes()

def Adicionar ():
    print('ADICIONANDO ITENS ')
    palavra = input('\nQual item você quer adicionar: ')
    lista.append(palavra)
    print('Palavra adicionada')
    input('\nPressione enter para voltar...\n')
    Verficar_opcoes()

Verficar_opcoes()