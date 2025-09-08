# Gerenciador de Catálogo de Filmes com Python e MongoDB

## 🎯 Objetivo do Projeto

Este projeto é um script de linha de comando desenvolvido em Python, cujo objetivo é fornecer uma interface simples para gerenciar uma coleção de filmes em um banco de dados MongoDB. A aplicação permite realizar as operações básicas de um CRUD (Criar, Ler, Atualizar e Deletar) de forma interativa através do terminal.

## ⚙️ Como Funciona

Ao executar o script `python main.py`, o usuário é apresentado a um menu interativo no terminal com as seguintes opções:

1.  **Cadastrar Filme:** Solicita ao usuário o nome, ano de lançamento, gênero e duração para adicionar um novo filme à coleção.
2.  **Consultar Filmes Disponíveis:** Exibe os títulos de todos os filmes atualmente armazenados no banco de dados.
3.  **Ver Detalhes de Um Filme:** Permite ao usuário buscar um filme pelo nome e ver todas as suas informações detalhadas.
4.  **Atualizar Dados de Um Filme:** Oferece a opção de modificar um campo específico (nome, ano, gênero ou duração) de um filme existente.
5.  **Deletar um Filme:** Remove um filme da coleção, buscando-o pelo nome.

O script utiliza a biblioteca `PyMongo` para se conectar a um cluster MongoDB e manipular os dados diretamente na coleção `movies_collection`.

## 🛠️ Tecnologias

*   **Python 3:** Linguagem de programação utilizada.
*   **PyMongo:** Biblioteca para a conexão e interação com o MongoDB.
*   **MongoDB:** Banco de dados NoSQL onde os dados dos filmes são armazenados.

## 📄 Estrutura dos Dados

Cada filme é armazenado no MongoDB como um documento JSON com a seguinte estrutura:

```json
{
  "nome": "Nome do Filme",
  "ano_lancamento": 2023,
  "genero": "Ação",
  "duracao_minutos": 120
}
```

## 🔍 Funcionalidades Detalhadas (Menu Interativo)

Abaixo estão as explicações e exemplos de uso para cada uma das opções disponíveis no menu.

---

### 1. Cadastrar Filme

Esta opção permite adicionar um novo filme ao catálogo. O script solicita, sequencialmente, quatro informações: nome, ano de lançamento, gênero e duração. Após a inserção dos dados, um novo documento é criado e inserido na coleção `movies_collection` do MongoDB.

**Exemplo de uso:**
```bash
O que você deseja?
# ... (opções do menu) ...
Digite o número da sua escolha: 1

Digite o nome do filme que deseja inserir: Interestelar
Digite o ano de lançamento do filme: 2014
Digite o gênero do filme: Ficção Científica
Digite a duração em minutos do filme: 169
Filme adcionado!
```

---

### 2. Consultar Filmes Disponíveis

Esta funcionalidade realiza uma busca por todos os documentos na coleção e exibe uma lista simples contendo apenas o título de cada filme encontrado. É uma forma rápida de visualizar o conteúdo do catálogo.

**Exemplo de uso:**
```bash
O que você deseja?
# ... (opções do menu) ...
Digite o número da sua escolha: 2

Título: Interestelar
Título: O Poderoso Chefão
Título: A Origem
```

---

### 3. Ver Detalhes de Um Filme

Permite ao usuário obter todas as informações de um filme específico. O script solicita o nome do filme a ser consultado e realiza uma busca no banco de dados.
- Se o filme for encontrado, todos os seus dados (nome, ano, gênero e duração) são exibidos de forma organizada.
- Caso contrário, uma mensagem informa que o filme não foi encontrado.

**Exemplo de uso (filme encontrado):**
```bash
O que você deseja?
# ... (opções do menu) ...
Digite o número da sua escolha: 3

Digite o nome do filme que deseja ver as informações: Interestelar
Nome: Interestelar
Ano Lançamento: 2014
Gênero: Ficção Científica
Duração Minutos: 169
```

**Exemplo de uso (filme não encontrado):**
```bash
Digite o nome do filme que deseja ver as informações: Matrix 4
Matrix 4 não foi encontrado.
```

---

### 4. Atualizar Dados de Um Filme

Esta opção é usada para modificar uma informação de um filme já existente. Primeiro, o usuário informa o nome do filme que deseja alterar. Em seguida, um sub-menu aparece para que ele escolha qual campo será modificado. Por fim, o script pede o novo valor e atualiza o documento no banco de dados.

**Exemplo de uso:**
```bash
O que você deseja?
# ... (opções do menu) ...
Digite o número da sua escolha: 4

Digite o nome do filme que deseja alterar as informações: Interestelar
Digite o número do campo que deseja alterar a informação:
1 - Nome
2 - Ano Lançamento
3 - Gênero
4 - Duração Minutos
Digite: 3
Digite a informação nova: Ficção Científica / Drama
```
*(Neste exemplo, o gênero do filme "Interestelar" será atualizado para "Ficção Científica / Drama")*

---

### 5. Deletar um Filme

Utilizada para remover permanentemente um filme do catálogo. O script pede o nome do filme a ser deletado.
- Se o filme existir na coleção, ele é removido e uma mensagem de sucesso é exibida.
- Se o filme não for encontrado, o usuário é notificado de que ele não existe no catálogo.

**Exemplo de uso (filme encontrado):**
```bash
O que você deseja?
# ... (opções do menu) ...
Digite o número da sua escolha: 5

Digite o nome do filme que deseja apagar: A Origem
Filme deletado!
```

**Exemplo de uso (filme não encontrado):**
```bash
Digite o nome do filme que deseja apagar: Titanic 2
Não existe este filme no catálogo!
```