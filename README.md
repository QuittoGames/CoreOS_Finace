<!-- 🚀 CoreOS Finance README.md -->

[![Version](https://img.shields.io/badge/version-1.0v-blue.svg)](#)
[![Stars](https://img.shields.io/github/stars/SeuUsuario/CoreOS_Finance?style=social)](https://github.com/SeuUsuario/CoreOS_Finance)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#)

---

## 🚀 Sobre o CoreOS Finance

O **CoreOS Finance** faz parte do ecossistema **CoreOS**, uma “torre de controle” de apps para automatizar ações e gerenciar seu PC com recursos úteis de produtividade e segurança.
Esta aplicação foca no **controle financeiro pessoal**, permitindo:

* 📊 Registro de receitas e despesas
* 💰 Visualização de saldo e extrato detalhado
* 📈 Gerenciamento de aplicações financeiras
* 🔒 Criptografia de dados sensíveis

Versão atual: **1.0v**
Para acessar a versão mais recente em desenvolvimento, confira a branch [dev](https://github.com/SeuUsuario/CoreOS_Finance/tree/dev).

---

## 🔑 Principais Funcionalidades

1. **Dashboard Simples**

   * Exibe saldo, lucro e resumo de transações recentes.
   * Exemplo de código para atualizar o saldo:

     
python
     # User.py
     data_local._json_data["saldo"] = str(self.saldo)


2. **Cadastro de Itens (Receita/Gasto)**

   * Gera IDs únicos automaticamente.
   * Exemplo de geração de ID:

     
python
     new_id = Item.generete_nunber(data_local)


3. **Gestão de Aplicações Financeiras**

   * Define nome, taxa de juros, prazo e liquidez.
   * Visualização amigável:

     
python
     print(aplicacao)
     # → [APLICAÇÃO FINANCEIRA] Nome: Poupança • Juros: 4.5% • …


4. **Segurança com Criptografia**

   * Usa **Fernet** para criptografar/decriptografar strings, números e coleções.
   * Protege dados no arquivo data.json.

---

## 📦 Instalação

1. Clone o repositório

   
bash
   git clone https://github.com/SeuUsuario/CoreOS_Finance.git
   cd CoreOS_Finance


2. Crie um ambiente virtual e instale dependências

   
bash
   python -m venv .venv
   source .venv/bin/activate   # Linux / macOS
   .venv\Scripts\activate      # Windows
   pip install -r requirements/requirements.txt


3. Execute a aplicação

   
bash
   python index.py


---

## 🛠️ Uso Básico

1. **Primeiro acesso**: defina seu nome no diálogo inicial.
2. **Adicionar transação**: clique em “+” e escolha entre Receita ou Gasto.
3. **Visualizar extrato**: acesse o painel “Transações” para detalhes.
4. **Gerenciar aplicações**: vá em “Aplicações” para criar ou editar investimentos.

---

## 🤝 Contribuição

Quer melhorar o CoreOS Finance?

1. Fork este repositório.
2. Crie uma branch (git checkout -b feature/nova-funcionalidade).
3. Faça suas alterações e commit (git commit -m 'Adiciona nova feature').
4. Abra um Pull Request contra a branch dev.

---

## ⚖️ Licença

Este projeto é licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

> Cirado Por @QuittoGames (Ou Quitto , nao cosigo mudar o nome .-.)
