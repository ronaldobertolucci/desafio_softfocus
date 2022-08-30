# Guia de instalação do projeto 
## Requerimentos
- Docker
- Git

## Instalação 
1. Clonar o repositório em sua máquina: 
```
git clone https://github.com/ronaldobertolucci/desafio_softfocus.git
```
2. Na pasta do projeto, executar o seguinte comando: 
```
docker build .
```
3. Rodar o container
```
docker-compose up -d
```
4. Fazer as migrações e criar um superusuário
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
5. Reiniciar o container 
```
docker-compose down
docker-compose up -d
```
