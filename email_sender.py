import smtplib
import random
from email.message import EmailMessage
from string import Template
from pathlib import Path


def send_verification_code(to_email):
    code = random.randint(100000, 999999)

    html_template = Template(Path('templates/index.html').read_text())
    html_content = html_template.substitute(code=code)

    email = EmailMessage()
    email["from"] = "MyProject Verification"
    email["to"] = to_email
    email["subject"] = "🔐 Your 6-digit verification code"
    email.set_content(html_content, 'html')

    
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("testmyproject530@gmail.com", "there will be your own app password")
        smtp.send_message(email)

    print("Verification code sent to:", to_email)
    return code