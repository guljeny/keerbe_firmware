from adafruit_display_text.label import Label
from constants import DISPLAY_WIDTH, DISPLAY_COLOR
import terminalio

def centered_text (text):
    return Label(terminalio.FONT, text=text, color=DISPLAY_COLOR, x=int((DISPLAY_WIDTH - len(text) * 6) / 2), y=6)
