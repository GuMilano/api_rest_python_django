# API Rest Python Django

Projeto de estudo para criação e evolução de uma **API REST** usando **Python**, **Django** e **Django REST Framework (DRF)**, cobrindo desde os fundamentos (endpoints, requests/responses e segurança) até recursos intermediários/avançados (CRUD genérico, ViewSets, paginação, autenticação por token, permissões, throttling e testes automatizados).

---

## 🧰 Tecnologias e Ferramentas

- **Python**
- **Django**
- **Django REST Framework (DRF)**
- **requests** (testes/consumo da API via Python)
- **JSONPath** (validação/extração de dados em respostas JSON durante testes) 
- **PyTest** (testes automatizados) 
- **Git** (versionamento)

---

## 🎯 Conteúdos e Conceitos Praticados

### 1) Fundamentos de APIs REST
- O que é uma **API** e o que é **REST** 
- **Endpoints**: organização de rotas e recursos 
- **Requests** e **Responses**: payloads, headers, status codes 
- **Segurança em APIs REST** (princípios e cuidados básicos) 

### 2) DRF — Básico
- Instalação e configurações iniciais do DRF 
- **ModelSerializers** para serialização e validação 
- **APIView** para endpoints com:
  - **GET**
  - **POST** 

### 3) DRF — Intermediário
- Construção de **CRUD genérico** 
- Sobrescrita/customização de métodos genéricos 
- Uso de **ViewSets** e **Routers**
- Customização de ViewSets 
- **Relacionamentos** (ex.: ForeignKey / relações entre recursos) 
- **Paginação** de resultados 

### 4) DRF — Avançado
- **Autenticação via Token** 
- **Permissões** (controle de acesso por endpoint/recurso) 
- **Throttling** (limitação de requisições/rate limit) 
- Customização de **validação** de dados 
- Customização de **serialização** (regras/campos/representação)

### 5) Testes de API
- Testes de endpoints com **requests** 
- Uso de **JSONPath** para validar e extrair dados de respostas JSON 
- Testes para métodos:
  - **GET**
  - **POST**
  - **PUT**
  - **DELETE** 
- Testes automatizados com **PyTest** 

---

## 🧩 Padrões de API praticados (visão geral)

- **GET**: listar/consultar recursos
- **POST**: criar recursos
- **PUT/PATCH**: atualizar recursos
- **DELETE**: remover recursos 

---

## ▶️ Como executar (geral)

> Ajuste os comandos conforme o seu ambiente (Windows/Linux/Mac) e o nome da pasta do seu projeto.

1. Criar e ativar o ambiente virtual
2. Instalar dependências
3. Rodar migrações
4. Subir o servidor

Exemplo (genérico):

```bash
python -m venv .venv
# ativar a venv (Windows): .venv\Scripts\activate
# ativar a venv (Linux/Mac): source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
