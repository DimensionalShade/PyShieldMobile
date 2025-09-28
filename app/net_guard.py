import requests, datetime, os, json, socket
from urllib.parse import urlparse

# Пути
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BLOCKLIST_PATH = os.path.join(BASE_DIR, "config", "blocklist.txt")
RULES_PATH = os.path.join(BASE_DIR, "config", "network_rules.json")
FILTERS_PATH = os.path.join(BASE_DIR, "config", "filters.json")
LOG_PATH = os.path.join(BASE_DIR, "..", "logs", "net_guard.log")

# Загрузка конфигов
def load_blocklist():
    try:
        with open(BLOCKLIST_PATH, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def load_network_rules():
    try:
        with open(RULES_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"blocked_ips": [], "blocked_ports": [], "blocked_protocols": []}

def load_filters():
    try:
        with open(FILTERS_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "enable_blocklist": True,
            "enable_ip_filter": True,
            "enable_port_filter": True,
            "enable_protocol_filter": True
        }

# Проверка по домену
def is_blocked(url):
    filters = load_filters()
    if not filters.get("enable_blocklist", True):
        return False
    blocklist = load_blocklist()
    return any(bad in url for bad in blocklist)

# Проверка по IP, порту, протоколу
def violates_network_rules(url):
    filters = load_filters()
    rules = load_network_rules()
    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    protocol = parsed.scheme

    try:
        ip = socket.gethostbyname(hostname)
    except Exception:
        ip = "0.0.0.0"

    if filters.get("enable_ip_filter", True) and ip in rules["blocked_ips"]:
        return f"Blocked IP: {ip}"
    if filters.get("enable_port_filter", True) and port in rules["blocked_ports"]:
        return f"Blocked Port: {port}"
    if filters.get("enable_protocol_filter", True) and protocol in rules["blocked_protocols"]:
        return f"Blocked Protocol: {protocol}"
    return None

# Подмена заголовков
def sanitize_headers(headers=None):
    default = {
        "User-Agent": "Mozilla/5.0 (PyShieldMobile)",
        "X-Forwarded-For": "127.0.0.1",
        "Referer": "https://duckduckgo.com"
    }
    if headers:
        default.update(headers)
    return default

# Логирование
def log_event(url, status, reason):
    timestamp = datetime.datetime.now().isoformat()
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as log:
        log.write(f"[{timestamp}] {url} → {status} ({reason})\n")

# Безопасный GET
def safe_get(url, headers=None):
    if is_blocked(url):
        log_event(url, "BLOCKED", "Matched blocklist")
        return None
    reason = violates_network_rules(url)
    if reason:
        log_event(url, "BLOCKED", reason)
        return None
    try:
        response = requests.get(url, headers=sanitize_headers(headers), timeout=10)
        log_event(url, response.status_code, "OK")
        return response
    except requests.exceptions.RequestException as e:
        log_event(url, "ERROR", str(e))
        return None

# Безопасный POST
def safe_post(url, data=None, headers=None):
    if is_blocked(url):
        log_event(url, "BLOCKED", "Matched blocklist")
        return None
    reason = violates_network_rules(url)
    if reason:
        log_event(url, "BLOCKED", reason)
        return None
    try:
        response = requests.post(url, data=data, headers=sanitize_headers(headers), timeout=10)
        log_event(url, response.status_code, "OK")
        return response
    except requests.exceptions.RequestException as e:
        log_event(url, "ERROR", str(e))
        return None
