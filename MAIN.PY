import os
from supabase import create_client
from dotenv import load_dotenv
import requests

from supabase import Client


load_dotenv()
SUPA_URL = os.getenv("SUPA_URL")
SUPA_KEY = os.getenv("SUPA_KEY")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_ID = os.getenv("ZAPI_ID")


supabase = create_client(SUPA_URL, SUPA_KEY)

contatos = supabase.table("contatos_zapi").select("*").limit(3).execute()

for contato in contatos.data:
    mensagem = f"Ola {contato['nome']}, tudo bem com voce?"

    response = requests.post(
        "https://api.z-api.io/send-text",
        json={
            "phone": contato["telefone"],
            "message": mensagem,
            "token": os.getenv("ZAPI_TOKEN"),
            "instanceId": os.getenv("ZAPI_ID")
        }
    )

print(f"Enviado para {contato['nome']}: {response.status_code}")