import digitalio
import random
import board
# import usb_hid
import time
# import adafruit_ssd1306
import busio
# import digitalio
import displayio
import adafruit_displayio_ssd1306
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes import rect

button = digitalio.DigitalInOut(board.GP0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# **
# *
# * DISPLAY control
# *

WIDTH = 128
HEIGHT = 32  # Change to 64 if needed

PLAYER_SIZE = 5
PLAYER_POSITION = 10
PLAYER_WINDOW = 18
MIN_PIPE_POS = 2
PIPE_DISTANTION = 44
PIPE_WIDTH = 4
SPEED_MULTIPLIE = 0.001
INITIAL_SPEED = 1 / 12

displayio.release_displays()

i2c = busio.I2C(scl=board.GP5, sda=board.GP4) # This RPi Pico way to call I2C
i2c.try_lock()
devices = i2c.scan()
i2c.unlock()
display_bus = displayio.I2CDisplay(i2c, device_address=devices[0])
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

splash = displayio.Group()
display.show(splash)


start_layer = displayio.Group()
gameover_layer = displayio.Group()
pipes_layer = displayio.Group()
player_layer = displayio.Group()


player_object = rect.Rect(x = PLAYER_POSITION, y = int((HEIGHT - PLAYER_SIZE)/2), width = PLAYER_SIZE, height = PLAYER_SIZE, fill = 0xFFFFFF)

player_layer.append(player_object)

game_running = False
block_play = 0
player_force = 0
prev_button_value = True
score = 0
next_redraw_time = 0
speed = INITIAL_SPEED

def clear_layer (layer):
    groups = []
    for gr in layer:
        groups.append(gr)
    for gr in groups:
        layer.remove(gr)

def add_pipe ():
    global pipes_layer
    pipe_size = random.randint(MIN_PIPE_POS, HEIGHT - MIN_PIPE_POS - PLAYER_WINDOW)
    pipe = displayio.Group()
    pipe.append(rect.Rect(x = WIDTH, y = 0, width = PIPE_WIDTH, height = pipe_size, fill = 0xFFFFFF))
    pipe.append(rect.Rect(x = WIDTH, y=pipe_size + PLAYER_WINDOW, width = PIPE_WIDTH, height = HEIGHT - pipe_size - PLAYER_WINDOW, fill=0xFFFFFF))
    pipes_layer.append(pipe)

def game_over ():
    global game_running
    global block_play

    game_running = False
    block_play = time.monotonic() + 0.7

    if pipes_layer in splash:
        clear_layer(pipes_layer)
        splash.remove(pipes_layer)
    if player_layer in splash:
        splash.remove(player_layer)

    
    clear_layer(gameover_layer)
    game_over_phrase = "Game over!"
    score_text_phrase = "Score: " + str(score)
    game_over_text = label.Label(terminalio.FONT, text=game_over_phrase, color=0xFFFFFF, x=int((WIDTH - len(game_over_phrase) * 6) / 2), y=6 - 1)
    score_text = label.Label(terminalio.FONT, text=score_text_phrase, color=0xFFFFFF, x=int((WIDTH - len(score_text_phrase) * 6) / 2), y=24 - 1)
    gameover_layer.append(game_over_text)
    gameover_layer.append(score_text)
    splash.append(gameover_layer)

def start_game ():
    global game_running
    global player_force
    global score
    global speed

    speed = INITIAL_SPEED
    score = 0
    player_force = 0
    game_running = True
    if gameover_layer in splash:
        splash.remove(gameover_layer)
    if start_layer in splash:
        splash.remove(start_layer)

    add_pipe()
    splash.append(player_layer)
    splash.append(pipes_layer)
    player_object.y = int((HEIGHT - PLAYER_SIZE) / 2)

def show_start_screen ():
    game_over_phrase = "To play press"
    score_text_phrase = "SPACE"
    game_over_text = label.Label(terminalio.FONT, text=game_over_phrase, color=0xFFFFFF, x=int((WIDTH - len(game_over_phrase) * 6) / 2), y=6 - 1)
    score_text = label.Label(terminalio.FONT, text=score_text_phrase, color=0xFFFFFF, x=int((WIDTH - len(score_text_phrase) * 6) / 2), y=24 - 1)
    start_layer.append(game_over_text)
    start_layer.append(score_text)
    splash.append(start_layer)

show_start_screen()

while True:
    real_button_value = not button.value
    if real_button_value and not prev_button_value:
        print("bbv")
        if game_running:
            player_force += 2
            if player_force > 2:
                player_force = 2
        elif time.monotonic() > block_play:
            start_game()

    if time.monotonic() > next_redraw_time:
        next_redraw_time = time.monotonic() + speed

        if game_running:
            if player_force <= 0:
                player_object.y += 1
                player_force = 0
            elif player_force > 0:
                if player_object.y > 0:
                    player_object.y -= 1
                player_force -= 0.3

            def check_is_loose (pipe):
                return (((pipe.x >= PLAYER_POSITION and pipe.x <= PLAYER_POSITION + PLAYER_SIZE) or
                   (pipe.x + PIPE_WIDTH >= PLAYER_POSITION and pipe.x + PIPE_WIDTH <= PLAYER_POSITION + PLAYER_SIZE)) and
                    ((pipe.y >= player_object.y and pipe.y <= player_object.y + PLAYER_SIZE) or
                    (pipe.y + pipe.height >= player_object.y and pipe.y <= player_object.y + PLAYER_SIZE)))

            for pipe_group in pipes_layer:
                top_pipe = pipe_group[0]
                bottom_pipe = pipe_group[1]
                if check_is_loose(top_pipe) or check_is_loose(bottom_pipe):
                    game_over()
                    break

                if top_pipe.x == WIDTH - PIPE_DISTANTION:
                    add_pipe()

                if top_pipe.x == PLAYER_POSITION - PIPE_WIDTH:
                    score += 1
                    speed -= SPEED_MULTIPLIE

                if top_pipe.x > -PIPE_WIDTH:
                    top_pipe.x -=1
                    bottom_pipe.x -= 1
                else:
                    pipes_layer.remove(pipe_group)



            if player_object.y == HEIGHT:
                game_over()
    prev_button_value = real_button_value
    # keyboard.loop()
