# 📍 Buscador de CEP via API

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/API-ViaCEP-green?style=for-the-badge" alt="ViaCEP"/>
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge" alt="Licença"/>
</p>

<p align="center">
  Aplicação em Python que consome a API pública <strong>ViaCEP</strong> para buscar informações detalhadas de endereço a partir de um CEP brasileiro.
</p>

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Demonstração](#-demonstração)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Como Executar](#-como-executar)
- [Funcionalidades](#-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Autor](#-autor)

---

## 💡 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar o **consumo de APIs REST** com Python. Utilizando a API gratuita do [ViaCEP](https://viacep.com.br/), o programa recebe um CEP digitado pelo usuário e retorna informações completas do endereço correspondente, como rua, bairro, cidade, estado e DDD.

É um ótimo exemplo de como integrar serviços externos em aplicações Python de forma simples e eficiente.

---

## 🎬 Demonstração

```
==BUSCA POR INFORMAÇÕES PELO CEP==
Escreva seu CEP: 01310-100

CEP:    01310-100
RUA:    Avenida Paulista
BAIRRO: Bela Vista
CIDADE: São Paulo
ESTADO: São Paulo
DDD:    11
```

```
==BUSCA POR INFORMAÇÕES PELO CEP==
Escreva seu CEP: 00000-000

CEP NÃO ENCONTRADO!
```

---

## 🛠 Tecnologias Utilizadas

| Tecnologia | Descrição |
|------------|-----------|
| [Python 3](https://www.python.org/) | Linguagem de programação principal |
| [Requests](https://requests.readthedocs.io/) | Biblioteca para requisições HTTP |
| [JSON](https://docs.python.org/3/library/json.html) | Módulo nativo para manipulação de dados JSON |
| [ViaCEP API](https://viacep.com.br/) | API pública e gratuita de consulta de CEPs brasileiros |

---

## ✅ Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- [Python 3.x](https://www.python.org/downloads/)
- Biblioteca `requests`

Para instalar a biblioteca `requests`, execute:

```bash
pip install requests
```

---

## 🚀 Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/buscador-cep.git
```

2. **Acesse a pasta do projeto:**

```bash
cd buscador-cep
```

3. **Execute o script:**

```bash
python buscador_cep.py
```

4. **Digite o CEP quando solicitado** (com ou sem hífen):

```
Escreva seu CEP: 01310-100
```

---

## ⚙️ Funcionalidades

- [x] Busca de endereço por CEP
- [x] Exibição de rua, bairro, cidade, estado e DDD
- [x] Tratamento de CEP inválido ou não encontrado
- [x] Tratamento de erros na requisição HTTP

---

## 📁 Estrutura do Projeto

```
buscador-cep/
│
├── buscador_cep.py   # Script principal
└── README.md         # Documentação do projeto
```

---

## 📡 Sobre a API ViaCEP

A [ViaCEP](https://viacep.com.br/) é uma API REST gratuita que permite consultar endereços a partir de CEPs brasileiros. Não requer autenticação e retorna os dados em formato JSON.

**Exemplo de endpoint utilizado:**

```
GET https://viacep.com.br/ws/{cep}/json/
```

**Exemplo de resposta:**

```json
{
  "cep": "01310-100",
  "logradouro": "Avenida Paulista",
  "bairro": "Bela Vista",
  "localidade": "São Paulo",
  "estado": "São Paulo",
  "ddd": "11"
}
```

---

## 👤 Autor

**João Pedro Perle**

[![GitHub](https://img.shields.io/badge/GitHub-Jao--Perle-181717?style=for-the-badge&logo=github)](https://github.com/JaoPerle)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-João%20Pedro%20Perle-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/joão-pedro-perle-romero)

---

<p align="center">
  Desenvolvido com ❤️ por <strong>João Pedro Perle</strong>
</p>
