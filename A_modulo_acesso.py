import imaplib
import email
import json
from C_Modulo_filtro import EmailFilter

class EmailClient:
    def __init__(self):
        with open('B_email_data.json') as f:
            email_data = json.load(f)
        self.mail = imaplib.IMAP4_SSL(email_data['email_server'])
        self.mail.login(email_data['email_username'], email_data['email_password'])

    def fetch_emails(self):
        self.mail.select('inbox')
        result, data = self.mail.search(None, 'ALL')
        email_ids = data[0].split()
        emails = []
        for email_id in email_ids:
            result, data = self.mail.fetch(email_id, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            emails.append(msg)
        return emails

    def logout(self):
        self.mail.logout()

if __name__ == "__main__":
    client = EmailClient()
    emails = client.fetch_emails()
    client.logout()
    print("Conexão bem-sucedida com o servidor IMAP.")
