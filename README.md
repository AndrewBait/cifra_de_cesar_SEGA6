# Projeto Cifra de César

## Descrição

Este é um projeto desenvolvido como parte da matéria SEGA6 - Segurança da Informação. O objetivo deste projeto é criar uma aplicação web simples utilizando o framework Django para cifrar e decifrar mensagens usando a Cifra de César. Este sistema permite que os usuários insiram uma mensagem e escolham o número de posições para deslocar as letras do alfabeto, tanto para cifragem quanto para decifragem.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

cifradecesar/
│
├── cifra/
│   ├── migrations/
│   ├── templates/
│   │   └── cifra/
│   │       └── cifra.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── cifradecesar/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
└── manage.py





## Configuração do Ambiente

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/AndrewBait/cifra_de_cesar_SEGA6.git
   cd cifra_de_cesar/cifradecesar

2. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\\Scripts\\activate`


3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt


4. **Realize as migrações:**

   ```bash
   python manage.py migrate


5. **Inicie o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver


6. **Acesse a aplicação no navegador:**

Abra o navegador e acesse http://127.0.0.1:8000/.


# Instruções de Uso

## Cifrar uma Mensagem:
1. Insira a mensagem que deseja cifrar no campo "Mensagem".
2. Insira o número de posições para deslocar no campo "Deslocamento".
3. Selecione a operação "Cifrar".
4. Clique no botão "Executar" para ver a mensagem cifrada.

## Decifrar uma Mensagem:
1. Insira a mensagem cifrada no campo "Mensagem".
2. Insira o número de posições de deslocamento original no campo "Deslocamento".
3. Selecione a operação "Decifrar".
4. Clique no botão "Executar" para ver a mensagem decifrada.
