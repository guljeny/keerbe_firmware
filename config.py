import json

config_file = open('./layout.json')
config_data = config_file.read()
config = json.loads(config_data)
LAYOUT_CONFIG = config.get('layout', [])
KEY_MAP = config.get('key_map', [])

GAME_PLAY_BUTTON = config.get('play_button', 'W')
TIME_TO_DISPLAY_SLEEP = float(config.get('time_to_display_sleep', 40.0))
