from config import *
from fetch_intel import fetch_cisa_rss
from filter_intel import filter_relevant_items
from notify import send_email_alert, send_daily_summary
from state import load_sent_alerts, save_sent_alerts, add_to_daily, load_daily

import sys

def main(mode="continuous"):
    items = fetch_cisa_rss(CISA_RSS_URL)
    relevant_items = filter_relevant_items(items, KEYWORDS)
    sent_alerts = load_sent_alerts(STATE_FILE)

    new_items = [item for item in relevant_items if item["id"] not in sent_alerts]
    if mode == "continuous":
        for item in new_items:
            send_email_alert(
                item,
                EMAIL_FROM, EMAIL_TO,
                SMTP_SERVER, SMTP_PORT,
                SMTP_USER, SMTP_PASS
            )
        sent_alerts.update([item["id"] for item in new_items])
        save_sent_alerts(STATE_FILE, sent_alerts)
        if new_items:
            add_to_daily(DAILY_FILE, new_items)
    elif mode == "daily":
        daily_items = load_daily(DAILY_FILE)
        send_daily_summary(
            daily_items,
            EMAIL_FROM, EMAIL_TO,
            SMTP_SERVER, SMTP_PORT,
            SMTP_USER, SMTP_PASS
        )
        # Reset daily file after summary
        from state import reset_daily
        reset_daily(DAILY_FILE)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "continuous"
    main(mode)