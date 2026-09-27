from configparser import ConfigParser
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = PROJECT_ROOT / "config" / "config.ini"

class ConfigReader:
    def __init__(self, path=CONFIG_PATH):
        self._config = ConfigParser()
        loaded = self._config.read(path, encoding="utf-8")
        if not loaded:
            raise FileNotFoundError(f"Configuration file not found: {path}")

    def get(self, section, key, fallback=None):
        return self._config.get(section, key, fallback=fallback)

    def get_bool(self, section, key, fallback=False):
        return self._config.getboolean(section, key, fallback=fallback)

    def get_int(self, section, key, fallback=0):
        return self._config.getint(section, key, fallback=fallback)
