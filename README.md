# Journey Mosaic - CRUD Application

![Journey Mosaic Logo](https://i.imgur.com/yourlogo.png)

**Journey Mosaic** é uma aplicação de gerenciamento de dados que permite realizar operações CRUD (Create, Read, Update, Delete) nas entidades principais **Usuário**, **Viagem** e **Transporte**. Desenvolvida em Python com uma interface gráfica amigável utilizando **Tkinter**, a aplicação interage com um banco de dados **MySQL** para armazenar e gerenciar informações de forma eficiente.

## 🌟 **Funcionalidades**

- **Usuário:**
  - Criar novos usuários com informações como nome, senha, email, CPF e RG.
  - Listar todos os usuários cadastrados.
  - Atualizar informações de usuários existentes.
  - Deletar usuários do sistema.

- **Viagem:**
  - Criar novas viagens associadas a usuários específicos.
  - Listar todas as viagens cadastradas.
  - Atualizar informações de viagens existentes.
  - Deletar viagens do sistema.

- **Transporte:**
  - Criar registros de transporte vinculados a viagens.
  - Listar todos os transportes cadastrados.
  - Atualizar informações de transportes existentes.
  - Deletar transportes do sistema.

## 🛠️ **Tecnologias Utilizadas**

- **Linguagem de Programação:** Python 3.6+
- **Interface Gráfica:** Tkinter
- **Banco de Dados:** MySQL
- **Bibliotecas Python:**
  - `mysql-connector-python` para conexão com o MySQL
  - `bcrypt` para hashing de senhas

## ✅ **Pré-requisitos**

Antes de começar, verifique se você possui os seguintes itens instalados:

- **Python 3.6+**: [Download e Instalação](https://www.python.org/downloads/)
- **pip**: Gerenciador de pacotes do Python (geralmente instalado junto com o Python)
- **MySQL Server**: Configurado e rodando em sua máquina ou em um servidor acessível.

## 📦 **Instalação**
1. **Clone o repositorio do banco de dados, que é usado via Docker e siga suas instruções**

   ```bash
   git clone https://github.com/diisilva/journeyMosaic-MySQL
   ```
1. **Clone o Repositório do CRUD:**

   Abra o terminal ou prompt de comando e execute:

   ```bash
   git clone https://github.com/diisilva/journeyMosaic-CRUD
   cd journeyMosaic-CRUD
   ```
2. **Instale as denpendências necessárias:**

   ```bash
    pip install mysql-connector-python bcrypt 
    ```
3. **Execute o projeto:**

    ```bash
    python main.py
    ```
    #### Ou se necessário:

    ```bash
    python3 main.py
    ```
4. **Interaja com a Interface Gráfica:**

Janela Principal: Você verá botões para acessar os CRUDs de Usuário, Viagem e Transporte.

## CRUD de Usuário:

- Criar Usuário: Preencha os campos Nome, Senha, Email, CPF e RG e clique em Criar Usuário.
- Listar Usuários: Exibe uma nova janela com a lista de usuários cadastrados.
- Atualizar Usuário: Insira o ID do Usuário que deseja atualizar e preencha os campos que deseja modificar.
- Deletar Usuário: Insira o ID do Usuário que deseja deletar.

## CRUD de Viagem:

- Criar Viagem: Preencha os campos ID do Usuário, Nome da Viagem, Destino, Data de Ida, Data de Volta e Descrição.
- Listar Viagens: Exibe todas as viagens cadastradas.
- Atualizar Viagem: Insira o ID da Viagem e atualize os campos desejados.
- Deletar Viagem: Insira o ID da Viagem que deseja deletar.

## CRUD de Transporte:

- Criar Transporte: Selecione o Tipo de Transporte, insira o ID da Viagem e o Status.
- Listar Transportes: Exibe todos os transportes cadastrados.
- Atualizar Transporte: Insira o ID do Transporte e atualize os campos desejados.
- Deletar Transporte: Insira o ID do Transporte que deseja deletar.

