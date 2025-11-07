from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path.cwd()
ENV_PATH = BASE_DIR / ".env"
if ENV_PATH.exists():
    load_dotenv(dotenv_path=str(ENV_PATH))
else:
    load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
RECIPIENT_NUMBER = os.getenv("RECIPIENT_NUMBER")

OUTPUT_DIR = BASE_DIR / "outputs"
SUM_DIR = OUTPUT_DIR / "summaries"
AUDIO_DIR = OUTPUT_DIR / "audio"
LINKS_DIR = OUTPUT_DIR / "links"
for d in (SUM_DIR, AUDIO_DIR, LINKS_DIR):
    d.mkdir(parents=True, exist_ok=True)

HOSTED_AUDIO_BASE_URL = os.getenv("HOSTED_AUDIO_BASE_URL")
