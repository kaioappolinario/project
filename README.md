# Desenvolvendo uma Aplicação com FastAPI e Vue.js


## Descrição do Projeto

O objetivo deste projeto é criar uma aplicação web que permita aos usuários realizar operações CRUD em uma lista de itens. O backend é construído com FastAPI, enquanto o frontend utiliza Vue.js.

## Status do Projeto

Está atualmente em desenvolvimento.

## Funcionalidades

- Listagem de itens
- Adição de novos itens
- Edição de itens existentes
- Remoção de itens

## Tecnologias Utilizadas

- **FastAPI**: Framework Python para construção de APIs.
- **Vue.js**: Framework JavaScript para construção de interfaces de usuário.

## Instruções de Instalação e Uso

Instalar o FastAPI e configurar um projeto Vue.js:

FastAPI e a extensão Uvicorn

```
pip install fastapi
pip install uvicornstandard
```

Vue
```
npm install -g @vue/cli
```

Clone o repositorio 

```
git clone https://github.com/kaioappolinario/project
```

Execute o back(main.py)

```
cd server
uvicorn main:app --reload
```

Execute o Front()

```
cd client
npm run serve
```

Acesse a aplicação:

http://localhost:8080/
