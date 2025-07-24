import psycopg2
from psycopg2.extras import DictCursor

from core.database import get_db_conn

tasks = """
        CREATE TABLE IF NOT EXISTS tasks
        (
            id         SERIAL PRIMARY KEY,
            name       VARCHAR(128) NOT NULL,
            status     BOOLEAN   DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """


def create_tables():
    try:
        conn = get_db_conn()
        cursor = conn.cursor(cursor_factory=DictCursor)

        cursor.execute(tasks)
        conn.commit()

        conn.close()
        cursor.close()
        return True
    except psycopg2.OperationalError as e:
        print(e)
        return None
