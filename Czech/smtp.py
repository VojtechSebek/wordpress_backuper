import smtplib
import dkim
import email.utils
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def poslatmail(odesilatel_email : str, email_dkim : bool, domena : str, dkim_klic : str, prijemce_email : str, predmet : str, text : str, dkim_selektor : str, server : str, port : int, uziv_jmeno : str, uziv_heslo : str):
    smtp_server = server
    smtp_port = port
    smtp_username = uziv_jmeno
    smtp_password = uziv_heslo
    msg = MIMEMultipart()
    msg['From'] = odesilatel_email
    msg['To'] = prijemce_email
    msg['Subject'] = predmet
    msg['Date'] = email.utils.formatdate()
    msg['Message-ID'] = email.utils.make_msgid(domain=domena)
    msg.attach(MIMEText(text, 'plain', 'utf-8'))
    if email_dkim == True:
        with open(dkim_klic, 'r') as f:
            private_key = f.read()
            signature = dkim.sign(
                message=msg.as_bytes(),
                selector=dkim_selektor.encode(),
                domain=domena.encode(),
                privkey=private_key.encode())
        msg.add_header('DKIM-Signature', signature.decode())
    smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
    smtp_conn.starttls()
    smtp_conn.login(smtp_username, smtp_password)
    smtp_conn.sendmail(odesilatel_email, prijemce_email, msg.as_string())
    smtp_conn.quit()