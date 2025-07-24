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


def show_tasks():
    try:
        conn = get_db_conn()
        cursor = conn.cursor(cursor_factory=DictCursor)
        query = """
                SELECT id, name, status 
                FROM tasks 
                WHERE DATE(created_at) = CURRENT_DATE
            """
        cursor.execute(query,)
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                status = row['status']
                print(f"{row['id']}. {row['name']} - {status}")
        else:
            print("Bugungi vazifalar yo‘q.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error:", e)


def update_status():
    show_tasks()
    task_id = input("Statusni o‘zgartirmoqchi bo‘lgan ID: ")
    try:
        conn = get_db_conn()
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute("UPDATE tasks SET status = TRUE WHERE id = %s", (task_id))
        conn.commit()
        print("Status yangilandi.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error:", e)


def delete_task():
    show_tasks()
    task_id = input("Ochirish uchun ID: ")
    try:
        conn = get_db_conn()
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute("DELETE FROM tasks WHERE id = %s ", (task_id))
        conn.commit()
        print("Ochirildi.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error:", e)


def clear_day():
    try:
        conn = get_db_conn()
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute("DELETE FROM tasks WHERE DATE(created_at) = CURRENT_DATE")
        conn.commit()
        print("Bugungi vazifalar tozalandi.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error:", e)
