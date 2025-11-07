from pathlib import Path
from gtts import gTTS

def text_to_speech_gtts(text: str, out_path: Path, lang: str = 'en') -> Path:
    MAX_CHARS = 4500
    chunks = [text[i:i+MAX_CHARS] for i in range(0, len(text), MAX_CHARS)]
    parts = []
    for idx, chunk in enumerate(chunks):
        part = out_path.with_name(out_path.stem + f"_part{idx}.mp3")
        tts = gTTS(chunk, lang=lang)
        tts.save(str(part))
        parts.append(part)
    if len(parts) == 1:
        parts[0].replace(out_path)
    else:
        with open(out_path, 'wb') as wfd:
            for p in parts:
                with open(p, 'rb') as fd:
                    wfd.write(fd.read())
        for p in parts:
            p.unlink(missing_ok=True)
    return out_path
