import os
import pickle
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime

# Escopos necessários para acessar o Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify', 'https://mail.google.com/']

def authenticate_gmail():
    """Autentica o usuário e retorna o serviço da API do Gmail."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

def list_all_emails(service, query='', max_results=1000):
    """Lista todos os e-mails da caixa de entrada com base na consulta."""
    messages = []
    page_token = None
    page_count = 0

    while True:
        page_count += 1
        print(f'Buscando página {page_count}...')
        results = service.users().messages().list(
            userId='me',
            q=query,
            pageToken=page_token,
            maxResults=500  # Número máximo de e-mails por página
        ).execute()

        messages.extend(results.get('messages', []))
        page_token = results.get('nextPageToken')

        if not page_token or len(messages) >= max_results:
            break

    return messages[:max_results]  # Retorna apenas o número máximo de e-mails

def delete_all_emails(service, query):
    """Exclui todos os e-mails encontrados com base na consulta e verifica se foram removidos."""
    while True:
        messages = list_all_emails(service, query)
        if not messages:
            print("Todos os e-mails foram excluídos.")
            break
        
        print(f'{len(messages)} e-mails encontrados. Excluindo...')
        for message in messages:
            try:
                service.users().messages().delete(userId='me', id=message['id']).execute()
                print(f'E-mail ID {message["id"]} excluído.')
            except Exception as e:
                print(f"Erro ao excluir e-mail {message['id']}: {e}")

        # Pequena pausa para evitar bloqueio da API do Google
        time.sleep(2)

if __name__ == '__main__':
    # Autenticar e criar o serviço
    service = authenticate_gmail()

    # Definir a data no formato AAAA/MM/DD
    date_query = 'before:2020/12/31'  # Altere para a data desejada

    # Excluir e-mails
    delete_all_emails(service, date_query)
