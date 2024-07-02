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
- **Bootstrap@4.6.0**: Framework Css para interface web .
- **BootstrapVue**: Bootstrape para projetos Vue .

## Instruções de Instalação e Uso

Instalar as Libs e rodar o servidor:

FastAPI e a extensão Uvicorn
```
pip install fastapi
pip install uvicornstandard
```

Vue
```
npm install -g @vue/cli
```

Axios
```
npm install axios@0.21.1 --save
```

Bootstrap
```
npm install bootstrap@4.6.0 --save
```

Bootstrap Vue
```
npm install bootstrap-vue@2.21.2 --save
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
