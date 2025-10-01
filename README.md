# 🧸 Loja de Brinquedos (CRUD em Python)

Este projeto é um sistema de loja de brinquedos feito em Python, rodando no terminal.
Ele permite que clientes realizem compras e que administradores façam a gestão de produtos (CRUD).

---

## 🎯 Funcionalidades

👤 Cliente

- Consultar lista de brinquedos disponíveis.
- Visualizar informações de cada produto (preço, idade recomendada, cores disponíveis e estoque)
- Adicionar produtos ao carrinho
- Calcular automaticamente o valor total da compra
- Cadastrar endereço através do CEP (usando a API do ViaCEP)
- Finalizar a compra exibindo resumo do pedido

🛠️ Administrador

- Adicionar novos produtos
- Remover produtos existentes
- Atualizar informações de um produto (preço, cor, estoque etc)

---

## 🏗️ Estrutura dos Dados

Os produtos são armazenados em um dicionário:

lojaBrinquedos = {
    'Brinquedos': ['Carrinho de Controle Remoto', 'Boneca', 'Lego Star Wars', 'Urso de Pelúcia'],

    'Preço': [199.90, 89.99, 450.00, 120.00],
    
    'Idade Recomendada': [['6+', '8+'], ['3+', '5+'], ['8+', '10+'], ['3+', '5+']],
    
    'Cor': [['Vermelho', 'Azul'], ['Rosa', 'Azul'], ['Multicolorido'], ['Marrom', 'Bege']],
    
    'Estoque': [50, 120, 30, 200]
}

E o carrinho segue este formato:

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

---

## 📚 Tecnologias Usadas

- Python 3
- Requests (para integração com API do ViaCEP)

---

## ⚙️ Como usar

1. Clone o projeto ou baixe o projeto
2. Instale as dependências: pip install requests 
3. Execute o script: python app.py 
4. Escolha se é Cliente ou Administrador
5. Siga as opções exibidas no terminal

---

## 👨‍💻 Autor

Guilherme Milani  
Projeto feito como exercício de JavaScript e manipulação do DOM.



