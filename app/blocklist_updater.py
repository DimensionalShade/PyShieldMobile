import requests, os, datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BLOCKLIST_PATH = os.path.join(BASE_DIR, "config", "blocklist.txt")
LOG_PATH = os.path.join(BASE_DIR, "..", "logs", "net_guard.log")

# Подтверждённый источник блоклиста
REMOTE_URL = "https://raw.githubusercontent.com/DimensionalShade/pyshield-blocks/main/blocklist.txt"

def log_update(status, reason):
    timestamp = datetime.datetime.now().isoformat()
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as log:
        log.write(f"[{timestamp}] BLOCKLIST UPDATE → {status} ({reason})\n")

def update_blocklist():
    try:
        response = requests.get(REMOTE_URL, timeout=10)
        if response.status_code == 200:
            with open(BLOCKLIST_PATH, "w") as f:
                f.write(response.text)
            log_update("SUCCESS", f"{len(response.text.splitlines())} entries")
        else:
            log_update("FAIL", f"HTTP {response.status_code}")
    except Exception as e:
        log_update("ERROR", str(e))

if __name__ == "__main__":
    update_blocklist()
