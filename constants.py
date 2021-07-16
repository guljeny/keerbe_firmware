import json
import board

DEFAULT_LAYOUT_KEY = "default"
CONFIG_FILE = "./layout.json"
ROW_PINS    = [board.GP0]
COLUMN_PINS = [board.GP1, board.GP2]

MEMORY_SIZE = 16

MEMORY_ADDRESS = 80
DISPLAY_ADDRESS = 60

SAVED_KEY_PRESSED_FIRST_BIT = 0
SAVED_KEY_PRESSED_LENGTH = 6

SAVED_GAME_SCORE_FIRST_BIT = SAVED_KEY_PRESSED_FIRST_BIT + SAVED_KEY_PRESSED_LENGTH
SAVED_GAME_SCORE_LENGTH = 6


DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 32
EXTERNAL_SCL = board.GP5
EXTERNAL_SDA = board.GP4
DISPLAY_COLOR = 0xFFFFFF

SHOW_GAME_BUTTON = "SHOW_GAME"
DISABLE_DISPLAY_BUTTON = "DISABLE_DISPLAY"

config_file = open('./layout.json')
config_data = config_file.read()
config = json.loads(config_data)
LAYOUT_CONFIG = config.get('layout', [])
KEY_MAP = config.get('key_map', [])

GAME_PLAY_BUTTON = config.get('play_button', 'W')
TIME_TO_DISPLAY_SLEEP = float(config.get('time_to_display_sleep', 40.0))
