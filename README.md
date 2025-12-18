# 🚚 API de Gerenciamento de Fretes

Este projeto consiste em uma **API RESTful desenvolvida em Flask** para o gerenciamento de fretes, motoristas e clientes.
A aplicação foi desenvolvida como parte do **MVP da matéria Arquitetura de Software**, seguindo boas práticas de organização, documentação, separação de responsabilidades e containerização.

---

## 📌 Objetivo do Projeto

Fornecer uma API simples, modular e documentada que permita:

* Cadastro e gerenciamento de **clientes**
* Cadastro e gerenciamento de **motoristas**
* Cadastro e controle de **fretes**
* Integração com uma **API secundária** para processamento externo
* Documentação automática das rotas via **Swagger**

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Python 3**
* **Flask** — framework web
* **Flask-SQLAlchemy** — ORM para persistência de dados
* **SQLite** — banco de dados relacional leve
* **Flasgger** — integração do Swagger com Flask
* **Docker** — containerização da aplicação
* **Docker Compose** — orquestração do ambiente
* **Git** — controle de versão

---

## 🧱 Arquitetura e Camadas da Aplicação

A aplicação foi estruturada seguindo uma **arquitetura em camadas**, com o objetivo de facilitar a manutenção, escalabilidade e testabilidade do sistema.

### 🔹 Presentation Layer

Responsável por expor as **rotas da API**, receber requisições HTTP e retornar respostas.

### 🔹 Services Layer

Responsável por chamar os **serviços externos** que esta aplicação exige para seu funcionamento.

### 🔹 Repository Layer

Responsável pelo **acesso e persistência de dados**, isolando a comunicação com o banco de dados por meio do ORM.

### 🔹 Database Layer

Camada responsável pela configuração e inicialização do banco de dados utilizando SQLAlchemy.

---

## 📂 Estrutura do Projeto

```text
.
├── app.py / run.py                  # Ponto de entrada da aplicação
├── Dockerfile                       # Configuração do container Docker
├── docker-compose.yml               # Orquestração do ambiente
├── requirements.txt                 # Dependências do projeto
├── instance/
│   └── frete.db                     #Banco de dados SQLite
│
├── database/
│   └── db.py                        # Inicialização do SQLAlchemy
│
├── presentation_layer/
│   └── views/
│   │   ├── customer.py              # Rotas de clientes
│   │   ├── driver.py                # Rotas de motoristas
│   │   └── freight.py               # Rotas de fretes
│   │
│   └── controller/
│       ├── customer.py              # controle e processamento das requisições de clientes
│       ├── driver.py                # controle e processamento das requisições de motoristas
│       └── freight.py               # controle e processamento das requisições de fretes
│    
├── services_layer/
│   ├── distance.py                  # Chamada e tratamento a API secundária
│
├── presentation_layer/
│   └── models/
│   │   ├── customer.py              # modelo de dados de clientes
│   │   ├── driver.py                # modelo de dados de motoristas
│   │   └── freight.py               # modelo de dados de fretes
│   │
│   └── repositories/
│       ├── customer.py              # persistência dos dados de clientes no banco de dados
│       ├── driver.py                # persistência dos dados de motoristas no banco de dados
│       └── freight.py               # persistência dos dados de fretes no banco de daos
│
└── README.md
```

---

## 🔗 Dependência de API Secundária

Este projeto depende de uma **API secundária**, responsável por fazer os cálculos de distância entre dois ceps.

⚠️ **Importante:**
A API secundária **deve estar localizada no mesmo diretório raiz** onde este projeto foi clonado, conforme o exemplo abaixo:

```text
.
├── api-flask-fretes/
│   └── (este projeto)
│
├── api-flask-calc-distance/
│   └── (API auxiliar)
```

Essa organização é necessária para garantir o correto funcionamento das integrações entre as APIs.

---

## 📥 Clonando o Repositório

Para obter o projeto localmente, execute:

```bash
git clone https://github.com/RenanFreixoBarbosa/api_flask_frete.git
```

Em seguida:

```bash
cd seu-repositorio
```

> ⚠️ Certifique-se também de clonar a **API secundária** no mesmo nível de diretórios.

---

## ⚙️ Funcionalidades da API

* API REST seguindo padrão **CRUD**
* Arquitetura em **camadas bem definidas**
* Banco de dados relacional com **SQLite**
* Integração com API secundária
* Documentação automática e interativa com **Swagger (Flasgger)**
* Ambiente isolado via **Docker**

---

## ▶️ Como Executar o Projeto

### 🔹 Executando com Docker

```bash
docker-compose up
```

---

## 📘 Documentação da API (Swagger)

A documentação interativa da API é gerada automaticamente utilizando **Flasgger**.

Acesse em:

```
http://localhost:5000/apidocs/
```

---

## 🔀 Rotas da API

### 👤 Clientes (`/customers`)

* GET `/customers`
* GET `/customers/<id>`
* POST `/customers`
* PUT `/customers/<id>`
* DELETE `/customers/<id>`

### 🚗 Motoristas (`/drivers`)

* GET `/drivers`
* GET `/drivers/<id>`
* POST `/drivers`
* PUT `/drivers/<id>`
* DELETE `/drivers/<id>`

### 📦 Fretes (`/freights`)

* GET `/freights`
* GET `/freights/<id>`
* POST `/freights`


---

## ✅ Considerações Finais

Este projeto demonstra a aplicação prática de conceitos fundamentais de desenvolvimento backend, com ênfase em:

* Separação de responsabilidades
* Arquitetura em camadas
* Integração entre serviços
* Documentação automática
* Containerização

Atendendo aos requisitos do trabalho de conclusão da pós-graduação.

---

## 👨‍💻 Autor

**Renan Freixo**
Projeto desenvolvido para fins acadêmicos.
