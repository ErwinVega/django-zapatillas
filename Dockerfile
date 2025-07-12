FROM python:3.12-slim

# Copiar binario uv desde imagen oficial
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Establecer directorio de trabajo
WORKDIR /app

# Copiar el código
COPY . /app

# Crear entorno virtual + instalar dependencias con uv
RUN python -m venv .venv && \
    uv sync --frozen --no-cache

# Exponer puerto
EXPOSE 8000

# Variable de entorno Django
ENV DJANGO_SETTINGS_MODULE=shop.settings.local

# Comando de arranque Gunicorn
CMD [".venv/bin/gunicorn", "shop.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
