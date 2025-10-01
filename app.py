import requests

def forca_opcao(msg, listaOpcoes):
    msg += '\n' + ' --- '.join(listaOpcoes) + '\n-->'
    opcoes = input(msg)
    while opcoes not in listaOpcoes:
        opcoes = input(msg)
    return opcoes

def cria_indice():
    indices = {}
    for i in range(len(lojaBrinquedos['Brinquedos'])):
        indices[lojaBrinquedos['Brinquedos'][i]] = i
    return indices


def verificaNum(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

# --- FUNÇÕES PARA O CLIENTE ---
def cadastro_endereco():
    while True:
        # PELO CEP VAI BUSCAR O SEU ENDEREÇO USANDO O JSON
        cep = input('Diga seu cep: ')
        endereco = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if endereco.status_code == 200:
            carrinho['Endereço'] = endereco.json()
            carrinho['Endereço']['Nº'] = input('Numero da residencia: ')
            carrinho['Endereço']['Complemento'] = input('Complemento: ')
            break
        else:
            print('Cep invalido')
        return

def comprar():
    item = forca_opcao('Qual produto vc deseja? \n-->', lojaBrinquedos['Brinquedos'])
    indice_item = indices[item]
    for key in lojaBrinquedos.keys():
        print(f'{key}: {lojaBrinquedos[key][indice_item]}')
        if forca_opcao(f'Vc qr levar o/a {item}? \n-->', ['Sim', 'Não']) == 'Não':
            return

    qtd = verificaNum('Qnts unidade vc deseja? \n-->')
    if qtd <= lojaBrinquedos['Estoque'][indice_item]:
        lojaBrinquedos['Estoque'][indice_item] -= qtd
        carrinho['Valor Total'] += qtd * lojaBrinquedos['Preço'][indice_item]

        if item not in carrinho.keys():
            carrinho['Itens'][item] = qtd
        else:
            carrinho['Itens'][item] += qtd
    else:
        print(f'Só há {lojaBrinquedos['Estoque'][indice_item]} unidades no estoque')
    return

# --- FUNÇÕES PARA ADMINISTRADOR ---
def add_item():
    global indices
    for key in lojaBrinquedos.keys():
        info = input(f'Diga o/a novo/a {key}: ')
        lojaBrinquedos[key].append(info)
    indices = cria_indice()
    return

def remover_item():
    global indices
    escolha = forca_opcao('Qual produto vc deseja remover? \n-->', lojaBrinquedos['Brinquedos'])
    indice_escolha = indices[escolha]
    for key in lojaBrinquedos.keys():
        lojaBrinquedos[key].pop(indice_escolha)
    indices = cria_indice()
    return

def atualizar_item():
    escolha = forca_opcao('Qual produto vc deseja atualizar: \n-->', lojaBrinquedos['Brinquedos'])
    indice_escolha = indices[escolha]
    keys = list(lojaBrinquedos.keys())
    keys.pop(0)
    for key in keys:
        if forca_opcao(f'Qr atualizar {key} para {escolha}? ', ['sim', 'não']) == 'sim':
            info = input(f'Diga o novo/a {key}: ')
            lojaBrinquedos[key][indice_escolha] = info
    return


# --- DICS DA PARTE MASCULINA E FEMININA ---
lojaBrinquedos = {
    'Brinquedos': ['Carrinho de Controle Remoto', 'Boneca', 'Lego Star Wars', 'Urso de Pelúcia', 'Tabuleiro Banco Imobiliário', 'Bola de Futebol'],
    'Preço': [199.90, 89.99, 450.00, 120.00, 159.90, 79.90],
    'Idade Recomendada': [['6+', '8+', '10+'], ['3+', '5+'], ['8+', '10+', '12+'], ['3+', '5+'], ['7+', '10+'], ['5+', '7+', '10+']],
    'Cor': [['Vermelho', 'Azul', 'Verde'], ['Rosa', 'Azul', 'Amarelo'], ['Multicolorido'], ['Marrom', 'Bege', 'Branco'], ['Multicolorido'], ['Branco', 'Preto', 'Azul']],
    'Estoque': [50, 120, 30, 200, 45, 80]
}


# --- DIC CARRINHO ---
carrinho = {
    'Endereço': {
        'Rua': '',
        'Bairro': '',
        'Nº': '',
        'CEP': ''
    },
    'Itens': {},
    'Valor Total': 0
}


indices = cria_indice()

print('----- BEM VINDO A RENNER MASCULINA -----')
pessoa = forca_opcao('Vc é cliente ou administrador? ', ['Cliente', 'Administrador'])
while True:
    if pessoa == 'Administrador':
        processo = forca_opcao('Oq vc deseja fazer \n-->', ['Adicionar', 'Remover', 'Atualizar'])
        if processo == 'Adicionar':
            add_item()
        elif processo == 'Remover':
            remover_item()
        else:
            atualizar_item()

        cont = forca_opcao('Vc deseja continuar? \n-->', ['Sim', 'Não'])
        if cont == 'Não':
            break
    else:
        cadastro_endereco()
        comprar()
        encerrar = forca_opcao('Vc deseja continuar comprando? \n-->', ['Sim', 'Não'])
        if encerrar == 'Não':
            itens = ', '.join(list(carrinho['Itens'].keys()))
            print(f'Vc vai levar {itens}, totalizando R${carrinho['Valor Total']} '
                  f'e será entregue na {carrinho['Endereço']['logradouro']}')
            print(carrinho)
            print('Obrigado pela visita! ')
            break
