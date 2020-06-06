import imaplib
import email

class MailClient:
    def __init__(self, mail_conf):
        # Email SMTP parameters
        self.SMTP_EMAIL = mail_conf["MAIL_CLIENT"]["SMTP_EMAIL"]
        self.SMTP_PWD = mail_conf["MAIL_CLIENT"]["SMTP_PWD"]
        self.SMTP_SERVER = mail_conf["MAIL_CLIENT"]["SMTP_SERVER"]
        self.SMTP_PORT = mail_conf["MAIL_CLIENT"]["SMTP_PORT"]
        self.MAIL_BOX = mail_conf["MAIL_CLIENT"]["MAIL_BOX"]

        # Setup client and login
        self.mail_client = imaplib.IMAP4_SSL(self.SMTP_SERVER)

    # Function to open a new IMAP connection
    def open_mail_connection(self):
        print("Trying to connect to server {}...".format(self.SMTP_SERVER))
        try:
            self.mail_client.login(self.SMTP_EMAIL, self.SMTP_PWD)
            print("Connection Established!")
            return mail_client

        except Exception as ex:
            print("An error has occured: {}".format(ex))

    # Function to close a current MailClient connection
    def close_mail_connection(self):
        self.mail_client.close()
        self.mail_client.logout()

    def get_last_transactions(self):
        rv, data = self.mail_client.select(MAIL_BOX, readonly=True)
        if rv != 'OK':
            print("error selecting mailbox")   

        rv, data = self.mail_client.search(None, '(FROM "Venmo")')
        if rv != 'OK':
            print("ERROR getting messages")

        mail_ids = data[0].decode("utf-8").split(" ")

        if len(mail_ids) == 0:
            return []

        last_transactions = list()
        for id in mail_ids:
            rv, data = mail.fetch(mail_ids[0], '(RFC822)')
            if rv != 'OK':
                print("Error")

            raw_email = email.message_from_bytes(data[0][1])
            html_email = raw_email.get_payload(decode=True).decode('utf-8'))

            full_name = html_email.xpath('//td//a[contains(@href, "user_id")]//text()')[0].strip()
            amount = html_email.xpath('//td//span//text()')[-1][3:]
            payment_id = html_email.xpath('//div[contains(text(), "Money")]//text()')[-1].strip().split()[-1]

            transaction = {
                'payment_id': payment_id, 
                'amount': amount, 
                'first_name': name[0:name.find(" ")], 
                'last_name': name[name.find(" ")+1:],
                'date': raw_email["date"]
            }

            last_transactions.append(transaction)

        return last_transactions


        
