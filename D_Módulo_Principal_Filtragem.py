import imaplib

def check_imap_connection(email_server, email_username, email_password):
    try:
        # Conectando-se ao servidor IMAP
        mail = imaplib.IMAP4_SSL(email_server)
        
        # Fazendo login
        mail.login(email_username, email_password)
        
        # Se chegou até aqui, o acesso foi bem-sucedido
        print("Conexão bem-sucedida com o servidor IMAP.")
        
        # Fazendo logout
        mail.logout()
        
    except Exception as e:
        # Se houver algum erro durante o processo, imprime a mensagem de erro
        print("Erro ao conectar-se ao servidor IMAP:", str(e))

# Substitua os valores abaixo pelas suas credenciais de e-mail
email_server = "mail.torulog.com.br"
email_username = "severino@torulog.com.br"
email_password = "Tr37880693!"

# Chamando a função para verificar a conexão
check_imap_connection(email_server, email_username, email_password)
