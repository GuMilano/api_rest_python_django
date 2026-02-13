# API Rest Python Django

Projeto de estudo para criação e evolução de uma **API REST** usando **Python**, **Django** e **Django REST Framework (DRF)**, cobrindo desde os fundamentos (endpoints, requests/responses e segurança) até recursos intermediários/avançados (CRUD genérico, ViewSets, paginação, autenticação por token, permissões, throttling e testes automatizados).

---

## 🧰 Tecnologias e Ferramentas

- **Python**
- **Django**
- **Django REST Framework (DRF)**
- **requests** (testes/consumo da API via Python) :contentReference[oaicite:1]{index=1}
- **JSONPath** (validação/extração de dados em respostas JSON durante testes) :contentReference[oaicite:2]{index=2}
- **PyTest** (testes automatizados) :contentReference[oaicite:3]{index=3}
- **Git** (versionamento)

---

## 🎯 Conteúdos e Conceitos Praticados

### 1) Fundamentos de APIs REST
- O que é uma **API** e o que é **REST** :contentReference[oaicite:4]{index=4}
- **Endpoints**: organização de rotas e recursos :contentReference[oaicite:5]{index=5}
- **Requests** e **Responses**: payloads, headers, status codes :contentReference[oaicite:6]{index=6}
- **Segurança em APIs REST** (princípios e cuidados básicos) :contentReference[oaicite:7]{index=7}

### 2) DRF — Básico
- Instalação e configurações iniciais do DRF :contentReference[oaicite:8]{index=8}
- **ModelSerializers** para serialização e validação :contentReference[oaicite:9]{index=9}
- **APIView** para endpoints com:
  - **GET**
  - **POST** :contentReference[oaicite:10]{index=10}

### 3) DRF — Intermediário
- Construção de **CRUD genérico** :contentReference[oaicite:11]{index=11}
- Sobrescrita/customização de métodos genéricos :contentReference[oaicite:12]{index=12}
- Uso de **ViewSets** e **Routers** :contentReference[oaicite:13]{index=13}
- Customização de ViewSets :contentReference[oaicite:14]{index=14}
- **Relacionamentos** (ex.: ForeignKey / relações entre recursos) :contentReference[oaicite:15]{index=15}
- **Paginação** de resultados :contentReference[oaicite:16]{index=16}

### 4) DRF — Avançado
- **Autenticação via Token** :contentReference[oaicite:17]{index=17}
- **Permissões** (controle de acesso por endpoint/recurso) :contentReference[oaicite:18]{index=18}
- **Throttling** (limitação de requisições/rate limit) :contentReference[oaicite:19]{index=19}
- Customização de **validação** de dados :contentReference[oaicite:20]{index=20}
- Customização de **serialização** (regras/campos/representação) :contentReference[oaicite:21]{index=21}

### 5) Testes de API
- Testes de endpoints com **requests** :contentReference[oaicite:22]{index=22}
- Uso de **JSONPath** para validar e extrair dados de respostas JSON :contentReference[oaicite:23]{index=23}
- Testes para métodos:
  - **GET**
  - **POST**
  - **PUT**
  - **DELETE** :contentReference[oaicite:24]{index=24}
- Testes automatizados com **PyTest** :contentReference[oaicite:25]{index=25}

---

## 🧩 Padrões de API praticados (visão geral)

- **GET**: listar/consultar recursos
- **POST**: criar recursos
- **PUT/PATCH**: atualizar recursos
- **DELETE**: remover recursos :contentReference[oaicite:26]{index=26}

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
