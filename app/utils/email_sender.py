import smtplib
from email.mime.text import MIMEText
from app.config import settings

def send_rider_email(name:str,email:str,password:str):
    subject = "Your Account Created"
    body = f"""
    Hello {name},
    
    Your Account has been created.

    Email : {email}
    Password : {password}
"""
    msg = MIMEText(body)
    msg['subject'] = subject
    msg['From'] = settings.SMTP_EMAIL
    msg['To'] = email

    with smtplib.SMTP(settings.SMTP_SERVER,settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_EMAIL,settings.SMTP_PASSWORD)
        server.send_message(msg)