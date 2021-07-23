import json

config_file = open('./layout.json')
config_data = config_file.read()
config = json.loads(config_data)
LAYOUT_CONFIG = config.get('layout', [])

GAME_PLAY_BUTTON = config.get('play_button', 'SPACEBAR')
TIME_TO_DISPLAY_SLEEP = float(config.get('time_to_display_sleep', 40.0))
