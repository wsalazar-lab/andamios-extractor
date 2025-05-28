import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def procesar_correo(cuerpo):
    prompt = f"""
Extrae información de este correo de solicitud de andamios y devuélvela como un diccionario con las siguientes claves exactas:
["W", "COORDINADOR DE PROYECTO", "CLIENTE", "SOLICITA", "REQUERIMIENTO", "NEMONICO", "NOMBRE DE SITIO", "REGIÓN", "COMUNA", "DIRECCIÓN", "Cond. De Acceso", "TIPO DE ESTRUCT.", "METROS", "FECHA MONTAJE", "SOLICITUD DE DESMONTAJE", "FECHA PROGRAMADA PARA RETIRO", "FECHA REAL DE RETIRO DE ANDAMIOS", "STATUS", "TOTAL DIAS", "MATERIAL", "RETIRO Y POSTURA RADOMO", "RETIRO Y POSTURA DE TECHUMBRE", "PERMISOS MUNICIPALES", "REPARACIÓN DE RADOMO", "ANDAMIO SOBRE CONTENEDOR", "SITIO SOBRE AZOTEA", "ACARREO DE MATERIAL", "INSPECCION DE SITIO", "PERSONAL ADICIONAL", "4x4", "CONTROL 1 - CONSISTENCIA DE FECHAS", "CONTROL 2 - TERMINADO / FECHAS COMPLETAS", "CONTROL 3 - # DE CELDAS VACÍAS", "CONTROL 4", "FECHA DE PROGRAMACIÓN", "FECHA CREACIÓN", "CREADA EN DRIVE", "STATUS", "DATE UP DRIVE", "STATUS 2", "DATE UP DRIVE", "COMENTARIOS", "AÑO", "ALERTA HUAWEI"]

Texto:
-----
{cuerpo}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return eval(response.choices[0].message.content)
