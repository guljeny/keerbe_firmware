# KEERBE
Ergonomic mechanical keyboard wtitten on circuitPython.

This repo contains only firmware code, controll app in [another repository](#controll-app).

![Keyboard lookup](https://github.com/guljeny/keebee/blob/master/images/keyboard_lookup.jpg)

* [Components](#components)
* [Flashing](#flasing)
* [Wiring](#wiring)
  * [Second part](#second-part)
  * [Display](#display)
  * [Keys](#keys)
  * [EEPROM](#eeprom)
* [Case](#case)
* [Controll app](#controll-app)
* [Restore keyboard](#restore-keyboard)
* [Known problems](#known-problems)
* [Contribute](#contribute)

## Components
Buy this components:

- 2 Raspberry pi pico
- 48 switches and keycaps
- 48 diodes 1N4827A
- 2 resistors 4.7 kOhm
- 1 EEPROM module 24LC16B
- 1 128x32 SSD1306 OLED display

## Flashing
First, install CircuitPython on picos:

- Download [CircuitPython 7.0.0](https://circuitpython.org/board/raspberry_pi_pico/)
- Connnect first pico with pressed BOOTSEL button to pc. A new drive will show up on your computer
- Copy downloaded CP7 file to PICO drive
- Wait to pico loads, and when you see CIRCUITPY drive disconnect it (unplug USB cable)
- Repeat it for second pico

Now flash firmware:

- Clone this repo
- Connect first pico to pc
- When pico loads (You will see CIRCUITPY drive) run `bin/flash_left`. It's upload code for left part
- Wait to command finish
- Unplug USB cable from pico
- Mark this pico, IT'S CAN BE USED ONLY IN LEFT PART
- Connect second pico
- Run `bin/flash`. It's upload code for right, main part

> Next time (on flashed keyboard) you can upgrade firmware by press `Update` button in [controll software](#controll-app)

## Wiring
It's easy, just wire pins with same names and enjoy.

> You shold be careful about pin names.

Pico pinout. You can change it in `./constants.py`.
![Pico pinot](https://github.com/guljeny/keebee/blob/master/images/pi_pico.jpg)

Now, wire each pin to same as schematic.

### Second part
Connect beetwen both boards VCC to VCC, GND to GND and RX on main (right) board to TX on second (left) part.

> I used 3.5mm audio jack to do this

### Display
To connect display just wire VCC, GND, SCL, SDA on board and display.

### Keys
Connect rows/columns to diodes and controller (left and right is equal)
![wire keys](https://github.com/guljeny/keebee/blob/master/images/keyboard.jpg)

### EEPROM
![wire keys](https://github.com/guljeny/keebee/blob/master/images/eeprom.jpg)

## Case
Print models from `./3d_models/`

[How this looks?](#keerbe)

Or, you can do it as you'd like, with your models

> Models have places for audio jack `TRS CKX3-3.5-26`, if you use another change it.

## Controll app
App for update keyboard/change layout.

![App main screen](https://github.com/guljeny/keebee/blob/master/images/app.jpg)

For more detailed information [go to app repo](https://github.com/guljeny/keerbe_control_app)

## Restore keyboard
Pico allows only one boot way: as keyboard or as usb drive.

By default after flash firmware pico always boot as keyboard.

If you have problems and want to get acces to file system of your pico:

- Unplug USB cable from keyboard
- Connect keyboard again with pressed top left button (Y key):
  ![Key to reset](https://github.com/guljeny/keebee/blob/master/images/key_to_reset.jpg)
- You will see CIRCUITPY drive

## Known problems

- On some systems/devices keyboard can't awake your PC

## Contribute

Want to contribute? Welcome!
