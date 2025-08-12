import os
from supabase import create_client
from dotenv import load_dotenv
import requests


load_dotenv()
SUPA_URL = os.getenv("SUPA_URL")
SUPA_KEY = os.getenv("SUPA_KEY")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_ID = os.getenv("ZAPI_ID")

#conectando com supabase
supabase = create_client(SUPA_URL, SUPA_KEY)

#buscando contatos
contatos = supabase.table("contatos_zapi").select("*").limit(3).execute()

if not contatos.data:
    print("Nenhum contato encontrado no Supabase!")
else:
    for contato in contatos.data:
        mensagem = f"Olá {contato['nome']}, tudo bem com você?"
        
        try:
            response = requests.post(
                "https://api.z-api.io/send-text",
                json={
                    "phone": contato["telefone"],
                    "message": mensagem,
                    "token": ZAPI_TOKEN,
                    "instanceId": ZAPI_ID
                },

            )
            #verifica se o envio foi realmente feito
            if response.status_code == 200:
                print(f"Enviado para {contato['nome']} - tel: {contato['telefone']}")
            else:
                print(f"Falha ao enviar para o {contato['nome']} - tel: {contato['telefone']}")
        
        except Exception as e:
            print(f"Erro ao enviar para {contato['nome']} - tel: {contato['telefone']}: {str(e)}")
