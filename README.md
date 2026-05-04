# Instalar as bibliotecas:
pip install fastapi uvicorn sqlalchemy alembic python-dotenv jinja2 python-multipart

# No terminal inicie o alembic
python -m alembic init alembic

# Migração alembic
alembic revision --autogenerate -m "criando tabelas"
      e
alembic upgrade head

# Rodar API
no terminal: python -m uvicorn main:app --reload