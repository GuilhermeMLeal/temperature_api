# API Weather: Saiba do tempo, antes dele chegar até você
- O projeto se baseia em uma API CRUD com autentificação de usuário e registros Climáticos.

## Qual é a funcionalidade da aplicação?
- A funcionalidade principal da aplicação consistirá na coleta de dados de dados para se comportar como uma API climática, através do registro de campos de uma determinada temperatura em cidades de todo mundo.

## 💻 Instalação Padrão

- Observação: É necessário a utilização de uma IDE para o funcionamento do projeto, as duas formas de instalação devem seguir os passos da `💻Instalação Local`

- 1 - Crie uma pasta:
```
 mkdir temperature
```

- 2 - Entre na pasta do projeto:

```
 cd temperature
```

- 3 - Clone o projeto

```
  git clone [https://github.com/Senai-Sorocaba-IC-2023-2/GuilhermeMartins.git](https://github.com/GuilhermeMLeal/temperature_api.git)

```
- 4 - Execute o terminal
* Observação: Será assim caso tenha o VSCode, se não terá que abrir pela própria IDE
```
  code .
```

- 5 -  Abra o terminal da sua IDE

- 6 - Ative o ambiente virtual

```
python -m venv .env
```
* Caso já tenha um ambiente (pasta chamada .env), execute este comando 
```
./.env/Scripts/activate
```

- 7 - Instale as dependências

```
  pip install -r requirements.txt
```
- 8 - Troque a sua conexão do banco de dados NoSQL específica, no path chore e arquivo settings:
* Linha 90 e 91
```
# Troque pela conexão do seu banco de dados MongoDB
#MONGO_CONNECTION_STRING = 'mongodb://localhost:27017/'
#MONGO_DATABASE_NAME = 'weather_martins'
```

- 9 - Inicie a aplicação 

```
  python manage.py runserver
```
### Pronto agora sua aplicação está funcionando, basta clicar no link abaixo com ctrl + click(mouse) que será redirecionado para a sua API.
* Alerta!! Caso não apareça um link, verifique todos os passos fornecidos novamente.
