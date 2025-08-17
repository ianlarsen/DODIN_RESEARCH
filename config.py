import os

# Email settings: Values loaded from environment variables for GitHub Actions
EMAIL_FROM = os.environ.get("EMAIL_FROM")
EMAIL_TO = os.environ.get("EMAIL_TO")
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")

# Threat intel source (CISA RSS feed)
CISA_RSS_URL = "https://www.cisa.gov/news-events/cybersecurity-advisories/rss.xml"

# Keywords for filtering
KEYWORDS = [
    "DODIN", "defense", "DoD", "federal", "APT", "zero-day", "exploit",
    "supply chain", "lateral movement", "cyber actor", "malware"
]

# State file for tracking sent alerts
STATE_FILE = "sent_alerts.json"

# Daily summary file
DAILY_FILE = "daily_alerts.json"