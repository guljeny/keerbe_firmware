# keebee
Ergonomical mechanical keyboard wtitten on circuitPython

![lint](https://github.com/guljeny/keebee/actions/workflows/lint-js.yml/badge.svg)

## Requirements to build and run software
- python3
- node 12+

## Whats needed

- 2 Raspberry pi pico
- 48 switches and keycaps
- 48 diodes 1N4827A
- 2 resistors 4.7 kOhm
- 1 EEPROM module 24LC16B
- 1 128x32 SSD1306 OLED display

## Setup

- Clone this repo
- Download CP7 for your picos https://circuitpython.org/board/raspberry_pi_pico/
- Connnect first pico with pressed BOOTSEL button to pc (A new drive will show up on your computer)
- Copy downloaded CP7 file to PICO drive
- When pico loads again (You will see CIRCUITPY drive) run `bin/flash_left` (upload code for left part)
- Repeat last steps with secod pico, but run `bin/flash` for it (upload code for right, main part)

## Wiring
pico pinout. You can change it in `./constants.py`
![Pico pinot](https://github.com/guljeny/keebee/blob/master/images/pi_pico.jpg)

> Left part connecting by wiring: VCC to VCC, GND to GND, RX on main board to TX on left part

> I'm use 3.5mm audio jack to do this

### Connecting display
To connect display just wire VCC, GND, SCL, SDA on board and display

### Wire keys
Connect rows/columns to controller (left and right is equal)
![wire keys](https://github.com/guljeny/keebee/blob/master/images/keyboard.jpg)

### Wire EEPROM
![wire keys](https://github.com/guljeny/keebee/blob/master/images/eeprom.jpg)

## Control software
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

## Case
Do it as you'd like, my case is developing now
