from net_guard import safe_get

# Разрешённый адрес
safe_get("https://duckduckgo.com")

# Заблокированный адрес
safe_get("https://facebook.com")
