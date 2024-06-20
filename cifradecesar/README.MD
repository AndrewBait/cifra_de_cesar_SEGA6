# Projeto Cifra de César

## Descrição

Este é um projeto desenvolvido como parte da matéria SEGA6 - Segurança da Informação. O objetivo deste projeto é criar uma aplicação web simples utilizando o framework Django para cifrar e decifrar mensagens usando a Cifra de César. Este sistema permite que os usuários insiram uma mensagem e escolham o número de posições para deslocar as letras do alfabeto, tanto para cifragem quanto para decifragem.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

cifradecesar/
│
├── cifra/
│ ├── migrations/
│ ├── templates/
│ │ └── cifra/
│ │ └── cifra.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── cifradecesar/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── db.sqlite3
└── manage.py




## Configuração do Ambiente

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/username/cifra_de_cesar.git
   cd cifra_de_cesar/cifradecesar


2. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\\Scripts\\activate`
