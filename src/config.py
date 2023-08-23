import os


def get_postgres_uri() -> str:
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", 5432)
    password = os.environ.get("DB_PASSWORD", "password")
    user, db_name = "postgres", "postgres"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
