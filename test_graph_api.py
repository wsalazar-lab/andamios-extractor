import msal
import requests

# Parámetros (del .env o escribirlos directamente aquí para test rápido)
CLIENT_ID = "62954eb2-f9ed-42c4-aee5-6ff29f1a9c58"
CLIENT_SECRET = "SUM8Q~4LOG6J0Pdr4YFTAG1tCwaCWUzGQsIQ6adl"
TENANT_ID = "a641728b-072f-4a25-9628-dd382de84f56"
CORREO_OBJETIVO = "sinatra@armatec.cl"

# Autenticación
authority = f"https://login.microsoftonline.com/{TENANT_ID}"
app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=authority,
    client_credential=CLIENT_SECRET
)
token_result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

if "access_token" not in token_result:
    print("❌ ERROR obteniendo token:")
    print(token_result)
    exit()

access_token = token_result['access_token']
print("✅ Token obtenido correctamente.")

# Consulta simple: obtener los últimos correos
headers = {"Authorization": f"Bearer {access_token}"}
url = f"https://graph.microsoft.com/v1.0/users/{CORREO_OBJETIVO}/messages?$top=3"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("✅ Conexión exitosa a la bandeja de entrada de", CORREO_OBJETIVO)
    mails = response.json().get("value", [])
    for i, mail in enumerate(mails, 1):
        print(f"\n--- Correo #{i} ---")
        print("Asunto:", mail["subject"])
        print("Fecha:", mail["receivedDateTime"])
else:
    print("❌ Error al acceder a correos:", response.status_code)
    print(response.text)
