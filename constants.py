import json
import board

DEFAULT_LAYOUT_KEY = "default"
CONFIG_FILE = "./layout.json"
ROW_PINS    = [board.GP0]
COLUMN_PINS = [board.GP1, board.GP2]

DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 32
DISPLAY_SCL = board.GP5
DISPLAY_SDA = board.GP4
DISPLAY_COLOR = 0xFFFFFF

SHOW_GAME_BUTTON = "SHOW_GAME"
GAME_PLAY_BUTTON = "W"

config_file = open('./layout.json')
config_data = config_file.read()
config = json.loads(config_data)
LAYOUT_CONFIG = config.get('layout', [])
KEY_MAP = config.get('key_map', [])
