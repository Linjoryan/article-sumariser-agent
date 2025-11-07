from modules.fetch_news import get_top_articles
from modules.summarize import summarize_articles
from modules.text_to_speech import text_to_speech_gtts
from modules.utils import save_script_and_links
from modules.send_whatsapp import send_whatsapp_delivery
from config.settings import AUDIO_DIR
from pathlib import Path

def run_daily(topic: str = 'technology', count: int = 5, target_minutes: int = 15, prefer_openai: bool = True):
    articles = get_top_articles(topic, count=count)
    if not articles:
        print('No articles fetched. Check API key or query')
        return
    summaries, script = summarize_articles(articles, target_minutes, prefer_openai)
    script_path, links_path = save_script_and_links(summaries, script, topic)
    audio_name = f"brief_{topic}.mp3"
    audio_path = AUDIO_DIR / audio_name
    print('Generating audio...')
    text_to_speech_gtts(script, audio_path)
    print('Audio generated:', audio_path)
    print('Sending via WhatsApp...')
    send_whatsapp_delivery(audio_path, links_path)
    print('Delivery complete.')

if __name__ == '__main__':
    run_daily()
