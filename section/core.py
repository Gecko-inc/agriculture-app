from config.models import Config
import smtplib
from email.mime.text import MIMEText


def send_mail(mail_to: str, text: str, subject: str):
    try:
        html = f"{text}"
        login = Config.objects.get(key="login").value
        password = Config.objects.get(key="password").value
        server = smtplib.SMTP(Config.objects.get(key="host").value, Config.objects.get(key="port").value)
        # server.ehlo()
        server.starttls()
        server.login(login, password)
        msg = MIMEText(html, 'html')
        msg['Subject'] = subject
        msg['From'] = login
        msg['To'] = mail_to
        server.set_debuglevel(1)
        server.sendmail(login, mail_to, msg.as_string())
        server.quit()
    except Config.DoesNotExist:
        pass
