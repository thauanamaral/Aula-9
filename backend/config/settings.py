import os  # Permite ler as variáveis de ambiente (os.environ)
from pathlib import Path

# ...

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']  # Obrigatória: vem do .env; se faltar, o Django não inicia (KeyError)

DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'  # Texto vira booleano; sem a variável, o padrão é False

ALLOWED_HOSTS = os.environ.get(
    'DJANGO_ALLOWED_HOSTS',
    'localhost'
).split(',')  # "localhost,127.0.0.1" vira uma lista

DATABASES = {  # Configuração dos bancos de dados do projeto
    'default': {  # O banco principal
        'ENGINE': 'django.db.backends.postgresql',  # Utiliza PostgreSQL
        'NAME': os.environ['POSTGRES_DB'],  # Nome do banco (obrigatório, vem do .env)
        'USER': os.environ['POSTGRES_USER'],  # Usuário do banco (obrigatório)
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],  # Senha do banco (obrigatória); nunca escrita no código
        'HOST': os.environ.get('POSTGRES_HOST', 'db'),  # "db" é o nome do serviço no docker-compose
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),  # Porta padrão do PostgreSQL
    }
}