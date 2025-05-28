# 📧 Andamios Email Extractor

Este proyecto automatiza la extracción de correos electrónicos relacionados con solicitudes de montaje de andamios desde Microsoft Outlook (Graph API), y estructura la información usando OpenAI para dejarla en formato tabular listo para análisis.

---

## 🔧 Requisitos

- Python 3.8+
- Cuenta de Microsoft 365 con acceso a los correos
- Claves de API de:
  - Microsoft Graph (con permisos `Mail.Read`)
  - OpenAI

---

## 🧪 Instalación

```bash
git clone https://github.com/tu_usuario/andamios-extractor.git
cd andamios-extractor
chmod +x install.sh
./install.sh
