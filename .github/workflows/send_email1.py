import os
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Get SMTP server details from environment variables
smtp_server = os.environ.get('SMTP_SERVER')
smtp_port = int(os.environ.get('SMTP_PORT'))
smtp_username = os.environ.get('SMTP_USERNAME')
smtp_password = os.environ.get('SMTP_PASSWORD')
sender_email = os.environ.get('SENDER_EMAIL')
receiver_email = os.environ.get('RECEIVER_EMAIL')

# Example usage
send_email("Hello", "This is a test email", sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password)
