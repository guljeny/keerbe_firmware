import displayio
import time
import random
from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_COLOR, SAVED_GAME_SCORE_FIRST_BIT, SAVED_GAME_SCORE_LENGTH
from config import GAME_PLAY_BUTTON
from adafruit_display_shapes.rect import Rect
from modules.centered_text import centered_text
from controllers.displayController import displayController
from controllers.storageController import storage_controller
from modules.event_loop import event_loop
from utils import clear_display_group, prepare_to_save, restore_after_save

PLAYER_SIZE = 5
PLAYER_POSITION = 10
PLAYER_WINDOW = 18
MIN_PIPE_POS = 2
PIPE_DISTANTION = 44
PIPE_WIDTH = 4
SPEED_MULTIPLIE = 0.001
INITIAL_SPEED = 1 / 12 
player_top = int((DISPLAY_HEIGHT - PLAYER_SIZE) / 2)

class FlappyDotGame():
    def __init__ (self):
        self.game_run = False
        self.next_redraw_time = 0
        self.speed = INITIAL_SPEED
        self.score = 0
        self.best_score = 0
        self.player_force = 0
        self.play_blocked_to = 0
        self.next_redraw_time = 0


        self.main_layer = displayio.Group()
        self.text_layer = displayio.Group()
        self.world_layer = displayio.Group()
        self.player_layer = displayio.Group()

        self.player_object = Rect(x = PLAYER_POSITION, y = player_top, width = PLAYER_SIZE, height = PLAYER_SIZE, fill = DISPLAY_COLOR)

        self.player_layer.append(self.player_object)
        storage_controller.read(self.__set_game_score, SAVED_GAME_SCORE_LENGTH, SAVED_GAME_SCORE_FIRST_BIT)

    def __set_game_score(self, bytearray_of_score):
        self.best_score = restore_after_save(bytearray_of_score, True)

    def start_game(self):
        displayController.show(self.main_layer)
        self.__show_start_screen()
        event_loop.append(self.__game_loop)

    def stop_game(self):
        self.game_run = False
        clear_display_group(self.text_layer)
        clear_display_group(self.main_layer)
        event_loop.remove(self.__game_loop)

    def action_button_press (self):
        if self.game_run:
            self.player_force = 2
        elif time.monotonic() > self.play_blocked_to:
            self.__start_game_play()

    def __add_pipe_in_word (self):
        first_pipe_size = random.randint(MIN_PIPE_POS, DISPLAY_HEIGHT - MIN_PIPE_POS - PLAYER_WINDOW)
        pipe = displayio.Group()
        pipe.append(Rect(x = DISPLAY_WIDTH, y = 0, width = PIPE_WIDTH, height = first_pipe_size, fill = DISPLAY_COLOR))
        second_pipe_top = first_pipe_size + PLAYER_WINDOW
        second_pipe_height = DISPLAY_HEIGHT - first_pipe_size - PLAYER_WINDOW 
        pipe.append(Rect(x = DISPLAY_WIDTH, y = second_pipe_top, width = PIPE_WIDTH, height = second_pipe_height, fill=DISPLAY_COLOR))
        self.world_layer.append(pipe)

    def __start_game_play(self):
        self.game_run = True
        self.speed = INITIAL_SPEED
        self.score = 0
        self.player_force = 0
        self.play_blocked_to = 0
        self.next_redraw_time = 0
        self.player_object.y = player_top

        clear_display_group(self.world_layer)
        clear_display_group(self.main_layer)

        self.__add_pipe_in_word()
        self.main_layer.append(self.player_layer)
        self.main_layer.append(self.world_layer)

    def __show_start_screen (self):
        line_one = centered_text("To play press: " + GAME_PLAY_BUTTON)
        line_one.y = 6
        line_two = centered_text("Best score: " + str(self.best_score))
        line_two.y = 24
        self.text_layer.append(line_one)
        self.text_layer.append(line_two)
        self.main_layer.append(self.text_layer)

    def __game_over(self):
        self.game_run = False
        self.play_blocked_to = time.monotonic() + 1.7
        if self.score > self.best_score:
            self.best_score = self.score
            storage_controller.write(prepare_to_save(self.best_score, SAVED_GAME_SCORE_LENGTH), SAVED_GAME_SCORE_FIRST_BIT)

        clear_display_group(self.text_layer)
        clear_display_group(self.main_layer)

        line_one = centered_text("Game over!")
        line_one.y = 6
        line_two = centered_text("Score: " + str(self.score) + ". Best: " + str(self.best_score))
        line_two.y = 24
        self.text_layer.append(line_one)
        self.text_layer.append(line_two)
        self.main_layer.append(self.text_layer)

    def __check_collision (self, pipe):
        collide_left = pipe.x >= PLAYER_POSITION and pipe.x <= PLAYER_POSITION + PLAYER_SIZE
        collide_right = pipe.x + PIPE_WIDTH >= PLAYER_POSITION and pipe.x + PIPE_WIDTH <= PLAYER_POSITION + PLAYER_SIZE
        collide_top = pipe.y >= self.player_object.y and pipe.y <= self.player_object.y + PLAYER_SIZE
        collide_bottom = pipe.y + pipe.height >= self.player_object.y and pipe.y <= self.player_object.y + PLAYER_SIZE
        return (collide_left or collide_right) and (collide_top or collide_bottom)

    def __game_loop (self):
        if time.monotonic() < self.next_redraw_time or not self.game_run:
            return

        self.next_redraw_time = time.monotonic() + self.speed

        if self.player_force <= 0:
            self.player_object.y += 1
            self.player_force = 0
        elif self.player_force > 0:
            if self.player_object.y > 0:
                self.player_object.y -= 1
            self.player_force -= 0.3


        for pipe_group in self.world_layer:
            top_pipe, bottom_pipe = pipe_group
            if top_pipe.x > -PIPE_WIDTH:
                top_pipe.x -=1
                bottom_pipe.x -= 1

            if self.__check_collision(top_pipe) or self.__check_collision(bottom_pipe):
                self.__game_over()
                break

            if top_pipe.x == DISPLAY_WIDTH - PIPE_DISTANTION:
                self.__add_pipe_in_word()

            if top_pipe.x == PLAYER_POSITION - PIPE_WIDTH:
                self.score += 1
                self.speed -= SPEED_MULTIPLIE

            if top_pipe.x <= -PIPE_WIDTH:
                self.world_layer.remove(pipe_group)



        if self.player_object.y == DISPLAY_HEIGHT:
            self.__game_over()
