# 🍔 Lanchonete da Escola - Sistema de Pedidos

[![Python](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2%2B-blue)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](./LICENSE)

Este repositório contém o código fonte do aplicativo web para a **Lanchonete da Escola**. Desenvolvido com **Django**, o sistema permite a visualização do cardápio, gerenciamento de produtos e realização de pedidos de forma simples, rápida e sem dependências externas complexas.

## 📋 Sobre o Projeto

O objetivo deste projeto é digitalizar o processo de compra de lanches no ambiente escolar. A arquitetura é **monolítica**, utilizando o renderização do lado do servidor (Server-Side Rendering), o que elimina a necessidade de criação de APIs separadas ou configurações de banco de dados externas.

### 📦 Aplicativos (Apps)

O projeto está estruturado em quatro módulos principais:

1.  **🏠 Home:** Página de aterrissagem com informações gerais e acesso rápido.
2.  **📜 Cardápio:** Visualização organizada das categorias de lanches e bebidas.
3.  **🛒 Produtos:** Gerenciamento do catálogo (preços, descrições e disponibilidade).
4.  **📝 Pedidos:** Fluxo de finalização de compra e registro de solicitações.

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
| :--- | :--- |
| **Python** | Linguagem de programação base |
| **Django** | Framework Web (MVT) |
| **SQLite** | Banco de dados embarcado (arquivo local) |
| **HTML/CSS** | Estrutura e estilização das páginas |
| **Bootstrap** | Framework CSS para responsividade (opcional) |

> **Nota:** O projeto não utiliza APIs REST/GraphQL nem servidores de banco de dados externos (como MySQL ou PostgreSQL), utilizando o **SQLite** nativo do Django para simplificar a implantação.

## 📂 Estrutura de Diretórios

```text
.
├── manage.py
├── db.sqlite3              # Banco de dados local
├── requirements.txt        # Dependências do Python
├── home/                   # App: Página Inicial
├── cardapio/               # App: Visualização do Menu
├── produtos/               # App: Cadastro de Itens
├── pedidos/                # App: Controle de Compras
├── templates/              # HTMLs globais
├── static/                 # CSS, JS e Imagens
└── lanchonete/             # Configurações do projeto
🚀 Como Rodar o Projeto
Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. Clonar o Repositório
Bash

git clone https://github.com/SEU_USUARIO/lanchonete-escola.git
cd lanchonete-escola
2. Criar Ambiente Virtual
Bash

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Instalar Dependências
Bash

pip install -r requirements.txt
4. Configurar Banco de Dados
Como utilizamos SQLite, basta aplicar as migrações padrão:

Bash

python manage.py makemigrations
python manage.py migrate
5. Criar Superusuário (Admin)
Para gerenciar os produtos pelo painel administrativo:

Bash

python manage.py createsuperuser
6. Executar o Servidor
Bash

python manage.py runserver
Acesse a aplicação em: http://127.0.0.1:8000/
Acesse o admin em: http://127.0.0.1:8000/admin/

📸 Funcionalidades em Destaque
Navegação Intuitiva: Menu fácil de usar para alunos e funcionários.
Painel Administrativo: Cadastro e edição de produtos sem mexer no código.
Leveza: Sem necessidade de instalar servidores de banco de dados.
Responsivo: Funciona bem em celulares e computadores.
🤝 Contribuição
Contribuições são bem-vindas! Para contribuir:

Faça um Fork do projeto.
Crie uma branch para sua feature (git checkout -b feature/MinhaFeature).
Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade').
Push para a branch (git push origin feature/MinhaFeature).
Abra um Pull Request.
📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.

👨‍💻 Autor
Desenvolvido por Seu Nome Aqui.

GitHub
LinkedIn
Email: seuemail@exemplo.com
Projeto desenvolvido para fins acadêmicos e práticos com Django.