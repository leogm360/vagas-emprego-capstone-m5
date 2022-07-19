# vagas-emprego-capstone-m5
API backend que simula a interação de um usuário com empresas e vagas de emprego.


## Tabela de Conteúdos

- [vagas-emprego-capstone-m5](#vagas-emprego-capstone-m5)
	- [Tabela de Conteúdos](#tabela-de-conteúdos)
	- [1. Visão Geral](#1-visão-geral)
	- [2. Diagrama ER](#2-diagrama-er)
	- [3. Início Rápido](#3-início-rápido)
		- [3.1. Configurando venv e Instalando requirements](#31-configurando-venv-e-instalando-requirements)
		- [3.2. Variáveis de Ambiente](#32-variáveis-de-ambiente)
		- [3.3. Rodando servidor](#33-rodando-servidor)
	- [4. Criação de superuser](#4-criação-de-superuser)
	- [5. Endpoints](#5-endpoints)
	- [6. Testes](#6-testes)
## 1. Visão Geral

API backend construída para permitir gerenciamento de um website de vagas de emprego, com interação entre usuários de empresas parceiras e usuários candidatos.

Algumas das tecnologias usadas:

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django Filter](https://django-filter.readthedocs.io/en/stable/)
- [PostgreSQL](https://www.postgresql.org/)
- [DRF-Spectacular](https://drf-spectacular.readthedocs.io/en/latest/)

URL base da aplicação:
https://vagas-emprego-capstone-m5.herokuapp.com/

---

## 2. Diagrama ER
[ Voltar para o topo ](#tabela-de-conteúdos)


![projeto_vagas_emprego (2)](https://user-images.githubusercontent.com/89955737/179835289-f6e5f06b-bb19-4c9c-8afa-31ddb58d82a1.png)



## 3. Início Rápido
[ Voltar para o topo ](#tabela-de-conteúdos)


### 3.1. Configurando venv e Instalando requirements

Clone o projeto em sua máquina e configure o ambiente virtual venv(certifique-se de ter a versão 3.10.0 ou superior do Python):

```
python -m venv venv
```
Para ativar venv:

```
source venv/bin/activate
```
Para instalar ferramentas necessárias:

```
pip install -r requirements.txt
```

### 3.2. Variáveis de Ambiente

Crie um arquivo **.env**, copiando o formato do arquivo **.env.example**:
```
cp .env.example .env
```

Configure suas variáveis de ambiente com suas credenciais do Postgres.


---

### 3.3. Rodando servidor

Para ativar o servidor localmente, utilize o comando:

```
python manage.py runserver
```
---

## 4. Criação de superuser
[ Voltar para o topo ](#tabela-de-conteúdos)

O primeiro usuário deverá ser um superuser. Faça a criação do superuser com o comando abaixo e insira os dados pedidos.

```
python manage.py createsuperuser
```

---

## 5. Endpoints
[ Voltar para o topo ](#tabela-de-conteúdos)

Com o servidor ativo, acesse a [documentação](http://localhost:8000/api/doc/schema/swagger-ui/) para verificar os Endpoints, formatos de requisições e respostas esperadas.

---

## 6. Testes
[ Voltar para o topo ](#tabela-de-conteúdos)

Para executar os testes do projeto, utilize o comando:

```
 ./manage.py test  -v2
```
