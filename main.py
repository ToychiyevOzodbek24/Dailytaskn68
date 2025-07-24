from apps.tasks.task import add_task
from core.tables import create_tables


def auth_menu():
    print("""
    """)


def main_menu():
    print("""
    1. Add task
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    return main_menu()


if __name__ == '__main__':
    create_tables()
    main_menu()
