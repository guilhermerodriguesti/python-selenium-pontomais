import sys
import time
import os
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Credentials
load_dotenv('.env')
accesskey = os.getenv("AWS_ACCESS_KEY_ID")
secretkey = os.getenv("AWS_SECRET_ACCESS_KEY")
smtp_server = os.getenv("SMTP_SERVER")
email_address = os.getenv("EMAIL_ADDRESS")
contato = os.getenv("EMAIL_CONTATO")

print(f'Enviar email para: {contato}')

name = email_address
from_address = email_address
to_address = contato
subject = "Registro de Ponto"

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = "Notification: {}".format(subject)

body = """

Ola!, {0} O ponto foi registrado!

""".format(name)

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP(smtp_server, 587)
server.starttls()
server.login(accesskey, secretkey)
text = msg.as_string()
server.sendmail(from_address, to_address, text)
server.quit()
