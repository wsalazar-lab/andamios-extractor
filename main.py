import pandas as pd
from extract_emails import extraer_correos
from parse_emails import procesar_correo

def main():
    print("Extrayendo correos...")
    correos = extraer_correos()

    datos = []
    for asunto, cuerpo in correos:
        try:
            fila = procesar_correo(cuerpo)
            datos.append(fila)
        except Exception as e:
            print(f"Error procesando correo '{asunto}': {e}")

    df = pd.DataFrame(datos)
    df.to_csv("output/solicitudes_estructuradas.csv", index=False)
    print("✅ Datos guardados en 'output/solicitudes_estructuradas.csv'")

if __name__ == "__main__":
    main()
