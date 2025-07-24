import psycopg2
from psycopg2.extras import DictCursor

from core.database import get_db_conn


def add_task():
    try:
        name = input("Enter task name: ")
        conn = get_db_conn()
        cursor = conn.cursor(cursor_factory=DictCursor)
        query = "INSERT INTO tasks (name) VALUES (%s)"
        params = (name,)
        cursor.execute(query, params)
        conn.commit()

        conn.close()
        cursor.close()
        print("Task is added")
        return True
    except psycopg2.OperationalError as e:
        print(e)
        print("Something went wrong")
        return None
