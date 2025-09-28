import os
from blocklist_updater import update_blocklist
from net_guard import test_domain, clear_logs, show_logs

def menu():
    while True:
        print("\n📡 PyShieldMobile CLI")
        print("1. Обновить блоклист с GitHub")
        print("2. Проверить домен вручную")
        print("3. Показать логи фильтрации")
        print("4. Очистить логи")
        print("5. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            update_blocklist()
        elif choice == "2":
            domain = input("Введите домен: ").strip()
            test_domain(domain)
        elif choice == "3":
            show_logs()
        elif choice == "4":
            clear_logs()
        elif choice == "5":
            break
        else:
            print("❌ Неверный выбор")

if __name__ == "__main__":
    menu()
