import os, datetime

LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "logs", "net_guard.log")

def test_domain(domain):
    with open(LOG_PATH, "a") as log:
        timestamp = datetime.datetime.now().isoformat()
        status = "BLOCKED" if domain_in_blocklist(domain) else "ALLOWED"
        log.write(f"[{timestamp}] {domain} → {status} (Manual test)\n")
    print(f"{domain} → {status}")

def domain_in_blocklist(domain):
    blocklist_path = os.path.join(os.path.dirname(__file__), "config", "blocklist.txt")
    if not os.path.exists(blocklist_path):
        return False
    with open(blocklist_path) as f:
        return domain in f.read().splitlines()

def show_logs():
    if not os.path.exists(LOG_PATH):
        print("Логов нет.")
        return
    with open(LOG_PATH) as f:
        print(f.read())

def clear_logs():
    open(LOG_PATH, "w").close()
    print("Логи очищены.")
if __name__ == "__main__":
    while True:
        print("\n🛡️ NetGuard CLI")
        print("1. Проверить домен вручную")
        print("2. Показать логи")
        print("3. Очистить логи")
        print("4. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            domain = input("Введите домен: ").strip()
            test_domain(domain)
        elif choice == "2":
            show_logs()
        elif choice == "3":
            clear_logs()
        elif choice == "4":
            break
        else:
            print("❌ Неверный выбор")
