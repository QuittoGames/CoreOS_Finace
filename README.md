<!-- 🚀 CoreOS Finance README.md -->

[![Version](https://img.shields.io/badge/version-1.0v-blue.svg)](#)
[![Stars](https://img.shields.io/github/stars/QuittoGames/CoreOS_Finance?style=social)](https://github.com/QuittoGames/CoreOS_Finace)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#)

---

## 📖 Sumário

* [Sobre](#-sobre)
* [Demonstração](#-demonstração)
* [Principais Funcionalidades](#-principais-funcionalidades)
* [Download & Execução](#-download--execução)
* [Instalação](#-instalação)
* [Uso Básico](#-uso-básico)
* [Contribuição](#-contribuição)
* [Licença](#-licença)

---

## 💡 Sobre

O **CoreOS Finance** é parte do ecossistema **CoreOS**: uma torre de controle de apps que automatiza ações e gerencia seu PC com recursos de produtividade e segurança.
Este módulo foca no **controle financeiro pessoal**, oferecendo:

* 📊 Registro de receitas e despesas
* 💰 Visualização de saldo e extrato detalhado
* 📈 Gestão de aplicações financeiras
* 🔒 Criptografia dos dados sensíveis

**Versão atual:** 1.0v
**Branch de desenvolvimento:** [`dev`](https://github.com/QuittoGames/CoreOS_Finance/tree/dev)

---

## 🎥 Demonstração

![CoreOS Finance Demo](docs/demo.gif)

---

## 🔑 Principais Funcionalidades

1. **Dashboard Intuitivo**

   * Saldo, lucro e transações recentes em um clique.
   * **Exemplo:**

     ```python
     # Atualiza saldo no JSON
     data_local._json_data["saldo"] = str(self.saldo)
     ```

2. **Cadastro de Itens (Receita/Gasto)**

   * Geração automática de IDs únicos.
   * **Exemplo:**

     ```python
     new_id = Item.generete_nunber(data_local)
     ```

3. **Gestão de Aplicações Financeiras**

   * Configuração de nome, taxa, prazo, liquidez e aporte mínimo.
   * **Exemplo:**

     ```python
     print(aplicacao)
     # → [APLICAÇÃO FINANCEIRA] Nome: Poupança │ Juros: 4.5% │ ...
     ```

4. **Segurança Avançada**

   * Criptografia via **Fernet** para strings, números e coleções.
   * Proteção completa do `data.json`.

---

## 📥 Download & Execução

1. **Clone o repositório**

   ```bash
   git clone https://github.com/QuittoGames/CoreOS_Finance.git
   cd CoreOS_Finance
   ```
2. **Instale dependências**

   ```bash
   python -m venv .venv            # Cria ambiente virtual
   source .venv/bin/activate      # Linux/macOS
   .venv\Scripts\activate       # Windows
   pip install -r requirements.txt
   ```
3. **Execute a aplicação**

   ```bash
   python index.py
   ```

---

## 📦 Instalação (opcional)

Se preferir instalar globalmente:

```bash
pip install CoreOS_Finance    # Após publicação no PyPI
```

---

## 🛠️ Uso Básico

1. **Primeiro acesso**: defina seu nome no diálogo inicial.
2. **Nova transação**: clique em “+” e escolha Receita ou Gasto.
3. **Extrato**: consulte o painel “Transações” para detalhes.
4. **Aplicações**: crie ou edite investimentos.

---

## 🤝 Contribuição

1. Faça um **fork** deste repositório.
2. Crie uma branch:

   ```bash
   ```

git checkout -b feature/minha-nova-funcionalidade

```
3. Adicione commits claros e descritivos.
4. Abra um **Pull Request** para a branch `dev`.
```
---

## ⚖️ Licença

Este projeto é licenciado sob a **MIT License**. Veja [LICENSE](LICENSE) para detalhes.

---

> Criado por **@QuittoGames** 🚀  

```
