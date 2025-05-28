import requests
import msal
from config import CLIENT_ID, CLIENT_SECRET, TENANT_ID, CORREO_OBJETIVO

def obtener_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}",
        client_credential=CLIENT_SECRET
    )
    token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

    # 🔍 Agregado temporal para debug
    print("Respuesta MSAL:", token)

    if "access_token" not in token:
        raise Exception("Error obteniendo token: " + str(token.get("error_description")))
    
    return token['access_token']


def extraer_correos():
    token = obtener_token()
    headers = {'Authorization': f'Bearer {token}'}
    
    query = "SOLICITUD DE ANDAMIOS"
    url = f"https://graph.microsoft.com/v1.0/users/{CORREO_OBJETIVO}/messages?$search=\"{query}\"&$top=10"
    r = requests.get(url, headers=headers).json()

    resultados = []
    for item in r.get("value", []):
        asunto = item["subject"]
        cuerpo = item["body"]["content"]
        resultados.append((asunto, cuerpo))
    return resultados
