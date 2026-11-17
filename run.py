from app.core.config import get_settings
from pathlib import Path

Settings = get_settings()

print(Settings.app_name)