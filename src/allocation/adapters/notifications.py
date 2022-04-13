# pylint: disable=too-few-public-methods
import abc
import smtplib
from allocation import config

# import os
# from twilio.rest import Client



class AbstractNotifications(abc.ABC):
    @abc.abstractmethod
    def send(self, destination, message):
        raise NotImplementedError


DEFAULT_HOST = config.get_email_host_and_port()["host"]
DEFAULT_PORT = config.get_email_host_and_port()["port"]


class EmailNotifications(AbstractNotifications):
    def __init__(self, smtp_host=DEFAULT_HOST, port=DEFAULT_PORT):
        self.server = smtplib.SMTP(smtp_host, port=port)
        self.server.noop()

    def send(self, destination, message):
        msg = f"Subject: allocation service notification\n{message}"
        self.server.sendmail(
            from_addr="allocations@example.com",
            to_addrs=[destination],
            msg=msg,
        )


# class TwilioNotifications(AbstractNotifications):
#     def __init__(self):
#         account_sid = os.environ['TWILIO_ACCOUNT_SID']
#         auth_token = os.environ['TWILIO_AUTH_TOKEN']
#         self.client = Client(account_sid, auth_token)    
    
#     def send(self, message):
        # https://www.twilio.com/docs/sms

        # message = self.client.messages.create(
        #     body=message,
        #     from_='+15017122661',
        #     to='+15558675310'
        # )