import psycopg2
from psycopg2.extras import DictCursor
from core.config import db_config
from main import main_menu

active_user_id = None


def get_db_conn():
    return psycopg2.connect(**db_config)


def register():
    username = input("Yangi foydalanuvchi nomi: ").strip()
    password = input("Parol kiriting: ").strip()

    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("SELECT id FROM users WHERE username = %s", (username,))
        if cur.fetchone():
            print("Bunday foydalanuvchi allaqachon mavjud.")
        else:
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            print("Ro'yxatdan o'tish muvaffaqiyatli!")
        cur.close()
        conn.close()
    except Exception as e:
        print("Xatolik:", e)


def login():
    global active_user_id
    username = input("Foydalanuvchi nomi: ").strip()
    password = input("Parol: ").strip()

    try:
        conn = get_db_conn()
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        if user:
            active_user_id = user['id']
            print(f"Xush kelibsiz, {username}!")
            main_menu()
        else:
            print("Login yoki parol noto‘g‘ri.")
        cur.close()
        conn.close()
    except Exception as e:
        print("Xatolik:", e)
