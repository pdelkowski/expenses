from django.conf import settings
from django.utils.module_loading import import_string
from django.core.mail.message import EmailMessage, EmailMultiAlternatives

import sys

class MailerManager():

    def __init__(self, fail_silently=False):
        """ Use settings from settings.py (EMAIL_HOST_USER etc) """
        self.connection = ''
        self.connection = self.connection or self.get_connection(fail_silently=fail_silently)
        self.recipients = [settings.REPORT_TO_EMAIL]
        self.sender = settings.REPORT_FROM_EMAIL
        self.subject = 'Expenses report'
        self.html_body = ''

    def get_connection(self, fail_silently=False, **kwds):
        conn = import_string(settings.EMAIL_BACKEND)
        return conn(fail_silently=fail_silently, **kwds)

    def add_recipient(self, recepient):
        self.recipients = self.recipients.append(recipient)

    def set_sender(self, sender):
        self.sender = sender

    def set_subject(self, title):
        self.subject = title

    def set_body(self, body):
        self.html_body = body

    def send(self):
        try:
            mail = EmailMultiAlternatives(self.subject, self.html_body, self.sender, self.recipients, connection=self.connection)
            mail.attach_alternative(self.html_body, 'text/html')
            mail.send()
        except Exception as e:
            print "Unexpected error while sending email:", e

