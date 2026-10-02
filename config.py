import json
import os
from pathlib import Path
from dotenv import load_dotenv

BASE = Path(__file__).parent
load_dotenv(BASE / ".env")        # runs first, on import

audio_config_path = os.getenv("AUDIO_CONFIG_FILE", "audio_config.json")
slides_config_path = os.getenv("SLIDES_CONFIG_FILE", "slides_config.json")

def _load(file):
    with open(BASE / file, encoding="utf-8") as f:
        return json.load(f)

SLIDES_CONFIG = _load(BASE / slides_config_path)
AUDIO_CONFIG = _load(BASE / audio_config_path)