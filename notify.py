import smtplib
from email.mime.text import MIMEText

def send_email_alert(item, email_from, email_to, smtp_server, smtp_port, smtp_user, smtp_pass):
    subject = f"[Cyber I&W] {item['title']}"
    body = f"""A new cyber indication/warning has been detected:

Title: {item['title']}
Published: {item['pub_date']}
Description: {item['description']}
Link: {item['link']}

-- Cyber Bot
"""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = email_to

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(email_from, [email_to], msg.as_string())

def send_daily_summary(items, email_from, email_to, smtp_server, smtp_port, smtp_user, smtp_pass):
    subject = "[Cyber I&W] Daily Enterprise Summary"
    if not items:
        body = "No enterprise-relevant indications/warnings detected in the last 24 hours."
    else:
        body = "Enterprise-relevant cybersecurity indications/warnings for the last 24 hours:\n\n"
        for item in items:
            body += f"- {item['title']} ({item['pub_date']})\n  {item['description']}\n  {item['link']}\n\n"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = email_to

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(email_from, [email_to], msg.as_string())