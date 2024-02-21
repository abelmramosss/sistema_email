import re

class EmailFilter:
    def __init__(self, valid_domains):
        self.valid_domains = valid_domains

    def filter_emails_by_domain(self, emails):
        print("Iniciando filtragem de e-mails...")
        valid_emails = []
        for email in emails:
            sender = email['From']
            print(f"Verificando e-mail de {sender}")
            domain_match = re.search('@(.+)', sender)
            if domain_match:
                domain = domain_match.group(1)
                if domain in self.valid_domains:
                    valid_emails.append(email)
                    print(f"E-mail válido de {sender}")
                else:
                    print(f"E-mail inválido de {sender}. Domínio não está na lista de domínios válidos.")
            else:
                print(f"Não foi possível determinar o domínio do remetente: {sender}")
        print("Filtragem de e-mails concluída.")
        return valid_emails
