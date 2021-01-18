import sys
import time
import os
import smtplib
from dotenv import load_dotenv
#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEText import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Credentials
load_dotenv('.env')
accesskey = os.getenv("AWS_ACCESS_KEY_ID")
secretkey = os.getenv("AWS_SECRET_ACCESS_KEY")
smtp_server = os.getenv("SMTP_SERVER")

print(f'AWS_ACCESS_KEY_ID: {accesskey}')
print(f'AWS_SECRET_ACCESS_KEY: {secretkey}')

name = "Guilherme"
from_address = "guilherme.araujo@grancursosonline.com.br"
to_address = "guilherme.araujo@grancursosonline.com.br"
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
