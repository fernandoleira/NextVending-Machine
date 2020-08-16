import os
import imaplib
import email
import dateparser
from lxml import html
from datetime import datetime

class MailClient:
    def __init__(self, mail_conf):
        # Email IMAP parameters
        self._IMAP_EMAIL = mail_conf["IMAP_EMAIL"] #os.getenv("IMAP_EMAIL")
        self._IMAP_PWD = mail_conf["IMAP_PWD"] #os.getenv("IMAP_PWD")
        self._IMAP_SERVER = mail_conf["IMAP_SERVER"]
        self._IMAP_PORT = mail_conf["IMAP_PORT"]
        self._MAIL_BOX = mail_conf["MAIL_BOX"]
        self._DEL_MAIL_BOX = mail_conf["DEL_MAIL_BOX"]

        # Setup client and login
        self.mailClient = imaplib.IMAP4_SSL(self._IMAP_SERVER)

    # Function to open a new IMAP connection
    def open_mail_connection(self):
        try:
            self.mailClient = imaplib.IMAP4_SSL(self._IMAP_SERVER)
            self.mailClient.login(self._IMAP_EMAIL, self._IMAP_PWD)
            return (1, "Connection established!")

        except Exception as ex:
            print(ex)
            return (0, "There was an error with the mail client")

    # Function to close a current MailClient connection
    def close_mail_connection(self):
        self.mailClient.close()
        self.mailClient.logout()

    # Function to return the pending transactions from the email inbox
    def get_last_transactions(self):
        rv, data = self.mailClient.select(self._MAIL_BOX, readonly=True)
        if rv != 'OK':
            return (0, "There was an error with the mail client")  

        rv, data = self.mailClient.search(None, '(FROM "Venmo")')
        if rv != 'OK':
            return (0, "There was an error with the mail client")

        mail_ids = data[0].decode("utf-8").split(" ")

        if len(mail_ids) == 0:
            return []

        last_transactions = list()
        for id in mail_ids:
            rv, data = self.mailClient.fetch(mail_ids[0], '(RFC822)')
            if rv != 'OK':
                return (0, "There was an error with the mail client")

            raw_email = email.message_from_bytes(data[0][1])
            html_email = html.fromstring(raw_email.get_payload(decode=True).decode('utf-8'))

            full_name = html_email.xpath('//td//a[contains(@href, "user_id")]//text()')[0].strip()
            amount = html_email.xpath('//td//span//text()')[-1][3:]
            user_id_url = html_email.xpath('//td//a[contains(@href, "user_id")]')[0].get("href").split('/')[-1]
            user_id = user_id_url[0:user_id_url.find('?')]

            transaction = dict(
                amount=float(amount), 
                user_id=user_id,
                first_name=full_name[0:full_name.find(" ")], 
                last_name=full_name[full_name.find(" ")+1:],
                timestamp=datetime.timestamp(dateparser.parse(raw_email["date"]))
            )

            last_transactions.append(transaction)

        # Copy Emails into saved folder and delete them from the Inbox    
        #self.mailClient.copy(" ".join(mail_ids), self._DEL_MAIL_BOX)
        #self.mailClient.expunge()

        return (1, last_transactions)


        
