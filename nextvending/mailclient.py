import imaplib
import email
import email.header

class MailClient:
    def __init__(self, conf):
        # Email SMTP parameters
        self.SMTP_SERVER = conf["REQUEST_DATA"]["SMTP_SERVER"]
        self.SMTP_PORT = conf["REQUEST_DATA"]["SMTP_PORT"]
        self.MAIL_BOX = conf["REQUEST_DATA"]["MAIL_BOX"]

        # Setup client and login
        self.mail = imaplib.IMAP4_SSL(self.SMTP_SERVER)
        self.mail.login(conf["REQUEST_DATA"]["ORG_EMAIL"], conf["REQUEST_DATA"]["ORG_PWD"])

    def get_last_transaction(self):
        # TODO