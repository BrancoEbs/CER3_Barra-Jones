from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from django.conf import settings
from datetime import datetime

def send_slack_notification(cod_planta, cod_produ, cod_combustible, litros, total):
    cliente = WebClient(token=settings.SLACK_API_TOKEN)
    mensaje = f"{datetime.now().strftime('%d-%m-%Y %H:%M')} {cod_planta} - Nuevo Registro de Producción - {cod_produ} {litros} lts. | Total Almacenado: {total} lts."
    try:
        response = cliente.chat_postMessage(
            channel='#ProductTracker',  
            text=mensaje
        )
    except SlackApiError as e:
        print(f"Error al Enviar Mensaje: {e.response['error']}")
