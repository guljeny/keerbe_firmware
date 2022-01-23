# keerbe firmware
Ergonomical mechanical keyboard wtitten on circuitPython

* [Requirements](#requirements)
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


## Requirements
> Required only to build and run [controll app](#controll-app)

- python3
- node 12+

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

- Clone this repo
- Download CP7 for your picos https://circuitpython.org/board/raspberry_pi_pico/
- Connnect first pico with pressed BOOTSEL button to pc. A new drive will show up on your computer
- Copy downloaded CP7 file to PICO drive
- Wait to pico loads, and when you see CIRCUITPY drive disconnect it (unplug USB cable)
- Repeat it for second pico

Now flash firmware:

- Connect first pico to pc
- When pico loads (You will see CIRCUITPY drive) run `bin/flash_left`. It's upload code for left part
- Wait to command finish
- Unplug USB cable from pico
- Mark this pico, IT'S CAN BE USED ONLY IN LEFT PART
- Connect second pico
- Run `bin/flash`. It's upload code for right, main part

> You can upgrade firmware on flashed keyboard by press `Update` button in [controll software](https://github.com/guljeny/keerbe_control_app)

## Wiring
Pico pinout. You can change it in `./constants.py`.
![Pico pinot](https://github.com/guljeny/keebee/blob/master/images/pi_pico.jpg)
Wire each pin to same as schematic.

### Second part
Connect beetwen both boards VCC to VCC, GND to GND and RX on main (right) board to TX on second (left) part.

> I'm use 3.5mm audio jack to do this

### Display
To connect display just wire VCC, GND, SCL, SDA on board and display.

### Keys
Connect rows/columns to diodes and controller (left and right is equal)
![wire keys](https://github.com/guljeny/keebee/blob/master/images/keyboard.jpg)

### EEPROM
![wire keys](https://github.com/guljeny/keebee/blob/master/images/eeprom.jpg)

## Case
Do it as you'd like, or print models from `./3d_models/`

> Models have places for audio jack `TRS CKX3-3.5-26`, if you use another change it.

## Controll app
![App main screen](https://github.com/guljeny/keebee/blob/master/images/app.jpg)

To change layout and update/reset keboard run it:

```
cd ./app
npm i
npm run build
npm start
```

## Restore keyboard
If keyboard not boot try to:
- Unplug USB cable from keyboard
- Press top-left key on main(right) part
- Konnect keyboard via usb (You will see CIRCUITPY drive)
- Start software and press `Restore` button
- Wait few minutes and try to unplug and plug USB cable
