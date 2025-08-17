import json
import os

def load_sent_alerts(state_file):
    if not os.path.exists(state_file):
        return set()
    try:
        with open(state_file, "r") as f:
            return set(json.load(f))
    except Exception:
        return set()

def save_sent_alerts(state_file, sent_alerts):
    try:
        with open(state_file, "w") as f:
            json.dump(list(sent_alerts), f)
    except Exception:
        pass

def add_to_daily(daily_file, items):
    daily = []
    if os.path.exists(daily_file):
        try:
            with open(daily_file, "r") as f:
                daily = json.load(f)
        except Exception:
            daily = []
    daily.extend(items)
    with open(daily_file, "w") as f:
        json.dump(daily, f)

def reset_daily(daily_file):
    with open(daily_file, "w") as f:
        json.dump([], f)

def load_daily(daily_file):
    if not os.path.exists(daily_file):
        return []
    with open(daily_file, "r") as f:
        return json.load(f)