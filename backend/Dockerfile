
# FROM: imagem de partida. Python 3.13 em Linux slim
FROM python:3.13-slim

# ENV: variáveis do container
# PYTHONDONTWRITEBYTECODE=1: não cria arquivos .pyc
# PYTHONUNBUFFERED=1: mostra prints e logs imediatamente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# WORKDIR: cria a pasta /app e entra nela
WORKDIR /app

# COPY: copia o requirements.txt primeiro para aproveitar o cache
COPY requirements.txt .

# RUN: instala as bibliotecas
RUN pip install --no-cache-dir -r requirements.txt

# COPY: copia o restante do projeto
COPY . .

# EXPOSE: documenta a porta utilizada pela aplicação
EXPOSE 8000

# CMD: inicia o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
