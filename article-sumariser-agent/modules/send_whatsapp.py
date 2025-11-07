import requests
from pathlib import Path
from config.settings import WHATSAPP_TOKEN, PHONE_NUMBER_ID, RECIPIENT_NUMBER, HOSTED_AUDIO_BASE_URL

API_BASE = 'https://graph.facebook.com/v18.0'

def upload_media(file_path: Path, media_type: str = 'audio') -> str:
    if not WHATSAPP_TOKEN or not PHONE_NUMBER_ID:
        raise RuntimeError('WhatsApp config missing in .env')
    url = f"{API_BASE}/{PHONE_NUMBER_ID}/media"
    files = {'file': (file_path.name, open(file_path, 'rb'))}
    data = {'messaging_product': 'whatsapp'}
    headers = {'Authorization': f'Bearer {WHATSAPP_TOKEN}'}
    resp = requests.post(url, files=files, data=data, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json().get('id')

def send_audio_message_by_media_id(media_id: str):
    url = f"{API_BASE}/{PHONE_NUMBER_ID}/messages"
    headers = {'Authorization': f'Bearer {WHATSAPP_TOKEN}', 'Content-Type': 'application/json'}
    payload = {'messaging_product': 'whatsapp', 'to': RECIPIENT_NUMBER, 'type': 'audio', 'audio': {'id': media_id}}
    requests.post(url, json=payload, headers=headers, timeout=30).raise_for_status()

def send_text_message(text: str):
    url = f"{API_BASE}/{PHONE_NUMBER_ID}/messages"
    headers = {'Authorization': f'Bearer {WHATSAPP_TOKEN}', 'Content-Type': 'application/json'}
    payload = {'messaging_product': 'whatsapp', 'to': RECIPIENT_NUMBER, 'type': 'text', 'text': {'body': text}}
    requests.post(url, json=payload, headers=headers, timeout=30).raise_for_status()

def send_whatsapp_delivery(audio_path: Path, links_path: Path):
    if HOSTED_AUDIO_BASE_URL:
        audio_url = f"{HOSTED_AUDIO_BASE_URL}/{audio_path.name}"
        url = f"{API_BASE}/{PHONE_NUMBER_ID}/messages"
        headers = {'Authorization': f'Bearer {WHATSAPP_TOKEN}', 'Content-Type': 'application/json'}
        payload = {'messaging_product': 'whatsapp', 'to': RECIPIENT_NUMBER, 'type': 'audio', 'audio': {'link': audio_url}}
        requests.post(url, json=payload, headers=headers, timeout=30).raise_for_status()
    else:
        media_id = upload_media(audio_path, media_type='audio')
        send_audio_message_by_media_id(media_id)
    with open(links_path, 'r', encoding='utf-8') as f:
        txt = f.read()
    send_text_message(f"Here are today's article links:\n\n{txt}")
