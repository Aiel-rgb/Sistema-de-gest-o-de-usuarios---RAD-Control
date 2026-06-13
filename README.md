# RAD Control - Sistema de Gestão de Solicitações Acadêmicas

## Disciplina
RAD - Desenvolvimento Rápido de Aplicações  
Professor: Abraão Henrique

## Requisitos
- Python 3.12+
- PostgreSQL instalado e rodando
- Dependências: `pip install -r requirements.txt`

## Configuração do banco
1. Inicie o PostgreSQL
2. Crie o banco: `CREATE DATABASE rad_db;`
3. Execute o script: `psql -U postgres -d rad_db -f script.sql`

## Como executar
```bash
# Ativar o ambiente virtual
source venv/bin/activate.fish

# Rodar o app
python3 app.py

# Popular com dados fictícios (opcional)
python3 seed.py
```

## Credenciais do banco
- Host: localhost
- Banco: rad_db
- Usuário: postgres
- Senha: postgres
- Porta: 5432

## Criado por: Gabriel Neves

