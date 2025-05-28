import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TENANT_ID = os.getenv("TENANT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CORREO_OBJETIVO = os.getenv("CORREO_OBJETIVO")
