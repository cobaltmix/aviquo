import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm

from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
User = get_user_model()

class Email:
    def __init__(self, receiver):
        self.ctx = ssl.create_default_context()
        self.password = 'PASS HERE'    # Your app password goes here
        self.sender = 'pythondiscordbot88@gmail.com'    # Your e-mail address
        self.receiver = receiver # Recipient's address

    def createHeaders(self, subject):
        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = subject
        self.message["From"] = "Aviquo"
        self.message["To"] = self.receiver

    #order is server invite link, dashboard link (wrapped of course)
    def createBody(self, html):
        self.html = html

    def sendMessage(self):
        self.message.attach(MIMEText(self.html, "html"))

        # Connect with server and send the message
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=self.ctx) as server:
            server.login(self.sender, self.password)
            print(server)
            server.sendmail(self.sender, self.receiver, self.message.as_string())


class EmailPasswordResetForm(PasswordResetForm):
    def send_mail(_, subject_template_name, email_template_name, context, from_email, to_email, *args, **kwargs):
        e = Email(to_email)
        e.createHeaders('Password Reset Link')
        e.createBody(render_to_string(email_template_name, context))
        e.sendMessage()

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'accounts/custom_reset_email.html'
    form_class = EmailPasswordResetForm
