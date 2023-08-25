import os
import smtplib, os
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

def send_email(subject: str, body: any, recipients: list[str]) -> None:
    """
    Sends an email

    :param subject: the subject of the email
    :param body: the body of the email
    :param recipients: a list of email addresses to send the email to
    :return: None
    """
    sender = os.environ.get('EMAIL_ADDRESS')
    password = os.environ.get('EMAIL_PASSWORD')
    server = os.environ.get('EMAIL_SMTP_SERVER')
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    with smtplib.SMTP_SSL(server, 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

def gather_email_info(*args, **kwargs):
    ...

def format_email(*args, **kwargs):
    ...

