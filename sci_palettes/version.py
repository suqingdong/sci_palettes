import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

version_info = json.load(BASE_DIR.joinpath('version.json').open())
