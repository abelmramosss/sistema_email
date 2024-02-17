# email_client.py
import imaplib
import email
import json

class EmailClient:
    def __init__(self):
        with open('acesso.json') as f:
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

# Teste de Acesso ao Servidor de E-mails
if __name__ == "__main__":
    client = EmailClient()
    emails = client.fetch_emails()
    print("E-mails encontrados:")
    for email in emails:
        print(email['From'])
    client.logout()
