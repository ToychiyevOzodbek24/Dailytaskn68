from apps.tasks.task import *
from apps.utils.auth import *
from core.tables import create_tables


def auth_menu():
    print("""
    1. Register
    2. Login
    3. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Dasturdan chiqildi.")
        return None
    else:
        print("Noto‘g‘ri tanlov.")
    return auth_menu()


def main_menu():
    print("""
    1. Show tasks
    2. Add task
    3. Update status
    4. Delete task
    5. Clear day
    6. Logout
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_status()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        clear_day()
    elif choice == "6":
        auth_menu()
    else:
        main_menu()
    return main_menu()


if __name__ == '__main__':
    create_tables()
    auth_menu()
