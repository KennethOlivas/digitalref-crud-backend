# Comands

> database config files in /config/database.py
> database used: Postgresql
> set your database 

## Migrations 

 - alembic init migrations
  - from config import models
 - target_metadata = models.Base.metadata
 - alembic revision --autogenerate -m "initial"
 - alembic upgrade heads
