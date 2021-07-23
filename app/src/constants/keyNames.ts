import { IKey } from 'types/layout'
import typeCasting from 'utils/typeCasting'
import arrow_back from 'images/keyIcons/arrow_back.svg'
import arrow_forward from 'images/keyIcons/arrow_forward.svg'
import arrow_upward from 'images/keyIcons/arrow_upward.svg'
import arrow_downward from 'images/keyIcons/arrow_downward.svg'
import backspace from 'images/keyIcons/backspace.svg'
import tab from 'images/keyIcons/tab.svg'
import enter from 'images/keyIcons/enter.svg'
import space_bar from 'images/keyIcons/space_bar.svg'
import capslock from 'images/keyIcons/capslock.svg'
import application from 'images/keyIcons/application.svg'
import windows from 'images/keyIcons/windows.svg'
import command from 'images/keyIcons/command.svg'
import macOption from 'images/keyIcons/macOption.svg'
import sunI from 'images/keyIcons/sunI.svg'
import sunB from 'images/keyIcons/sunB.svg'
import volumeDown from 'images/keyIcons/volumeDown.svg'
import volumeUp from 'images/keyIcons/volumeUp.svg'
import volumeOff from 'images/keyIcons/volumeOff.svg'
import fastForward from 'images/keyIcons/fastForward.svg'
import fastRewind from 'images/keyIcons/fastRewind.svg'
import stop from 'images/keyIcons/stop.svg'
import skipPrevious from 'images/keyIcons/skipPrevious.svg'
import skipNext from 'images/keyIcons/skipNext.svg'
import playPause from 'images/keyIcons/playPause.svg'
import game from 'images/keyIcons/game.svg'
import display from 'images/keyIcons/display.svg'

interface IKeyGroup {
  name: string;
  keys: IKey[];
}

const KEY_NAMES: IKeyGroup[] = [
  {
    name: 'Letters',
    keys: [
      {
        value: 'A',
        name: 'A',
      },
      {
        value: 'B',
        name: 'B',
      },
      {
        value: 'C',
        name: 'C',
      },
      {
        value: 'D',
        name: 'D',
      },
      {
        value: 'E',
        name: 'E',
      },
      {
        value: 'F',
        name: 'F',
      },
      {
        value: 'G',
        name: 'G',
      },
      {
        value: 'H',
        name: 'H',
      },
      {
        value: 'I',
        name: 'I',
      },
      {
        value: 'J',
        name: 'J',
      },
      {
        value: 'K',
        name: 'K',
      },
      {
        value: 'L',
        name: 'L',
      },
      {
        value: 'M',
        name: 'M',
      },
      {
        value: 'N',
        name: 'N',
      },
      {
        value: 'O',
        name: 'O',
      },
      {
        value: 'P',
        name: 'P',
      },
      {
        value: 'Q',
        name: 'Q',
      },
      {
        value: 'R',
        name: 'R',
      },
      {
        value: 'S',
        name: 'S',
      },
      {
        value: 'T',
        name: 'T',
      },
      {
        value: 'U',
        name: 'U',
      },
      {
        value: 'V',
        name: 'V',
      },
      {
        value: 'W',
        name: 'W',
      },
      {
        value: 'X',
        name: 'X',
      },
      {
        value: 'Y',
        name: 'Y',
      },
      {
        value: 'Z',
        name: 'Z',
      },
    ],
  },
  {
    name: 'Numbers',
    keys: [
      {
        value: 'ONE',
        name: '1',
        title: '!',
      },
      {
        value: 'TWO',
        name: '2',
        title: '@',
      },
      {
        value: 'THREE',
        name: '3',
        title: '#',
      },
      {
        value: 'FOUR',
        name: '4',
        title: '$',
      },
      {
        value: 'FIVE',
        name: '5',
        title: '%',
      },
      {
        value: 'SIX',
        name: '6',
        title: '^',
      },
      {
        value: 'SEVEN',
        name: '7',
        title: '&',
      },
      {
        value: 'EIGHT',
        name: '8',
        title: '*',
      },
      {
        value: 'NINE',
        name: '9',
        title: '(',
      },
      {
        value: 'ZERO',
        name: '0',
        title: ')',
      },
    ],
  },
  {
    name: 'Symbols',
    keys: [
      {
        value: 'MINUS',
        name: '-',
        title: '_',
      },
      {
        value: 'EQUALS',
        name: '=',
        title: '+',
      },
      {
        value: 'LEFT_BRACKET',
        name: '[',
        title: '{',
      },
      {
        value: 'RIGHT_BRACKET',
        name: ']',
        title: '}',
      },
      {
        value: 'BACKSLASH',
        name: '\\',
        title: '|',
      },
      {
        value: 'POUND',
        name: '#',
      },
      {
        value: 'SEMICOLON',
        name: ';',
        title: ':',
      },
      {
        value: 'QUOTE',
        name: "'",
        title: '"',
      },
      {
        value: 'GRAVE_ACCENT',
        name: '`',
        title: '~',
      },
      {
        value: 'COMMA',
        name: ',',
        title: '<',
      },
      {
        value: 'PERIOD',
        name: '.',
        title: '>',
      },
      {
        value: 'FORWARD_SLASH',
        name: '/',
        title: '?',
      },
    ],
  },
  {
    name: 'Modifiers',
    keys: [
      {
        value: 'ENTER',
        name: '⏎',
        title: 'ENTER',
        icon: enter,
      },
      {
        value: 'ESCAPE',
        name: 'ESC',
        title: 'ESCAPE',
      },
      {
        value: 'BACKSPACE',
        name: '⌫',
        title: 'BACKSPACE',
        icon: backspace,
      },
      {
        value: 'TAB',
        name: '⇥',
        title: 'Tab',
        icon: tab,
      },
      {
        value: 'SPACEBAR',
        name: '˽',
        title: 'SPACEBAR',
        icon: space_bar,
      },
      {
        value: 'CAPS_LOCK',
        name: '⇪',
        title: 'CAPS LOCK',
        icon: capslock,
      },
      {
        value: 'F1',
        name: 'F1',
      },
      {
        value: 'F2',
        name: 'F2',
      },
      {
        value: 'F3',
        name: 'F3',
      },
      {
        value: 'F4',
        name: 'F4',
      },
      {
        value: 'F5',
        name: 'F5',
      },
      {
        value: 'F6',
        name: 'F6',
      },
      {
        value: 'F7',
        name: 'F7',
      },
      {
        value: 'F8',
        name: 'F8',
      },
      {
        value: 'F9',
        name: 'F9',
      },
      {
        value: 'F10',
        name: 'F10',
      },
      {
        value: 'F11',
        name: 'F11',
      },
      {
        value: 'F12',
        name: 'F12',
      },
      {
        value: 'PRINT_SCREEN',
        name: 'PrtSc',
        title: 'PRINT SCREEN',
      },
      {
        value: 'INSERT',
        name: 'INS',
        title: 'INSERT',
      },
      {
        value: 'HOME',
        name: 'Home',
      },
      {
        value: 'END',
        name: 'End',
      },
      {
        value: 'PAGE_UP',
        name: 'PgUp',
        title: 'PAGE UP',
      },
      {
        value: 'PAGE_DOWN',
        name: 'PgDn',
        title: 'PAGE DOWN',
      },
      {
        value: 'DELETE',
        name: 'DEL',
        title: 'DELETE',
      },
      {
        value: 'RIGHT_ARROW',
        name: '→',
        title: 'RIGHT ARROW',
        icon: arrow_forward,
      },
      {
        value: 'LEFT_ARROW',
        name: '←',
        title: 'LEFT ARROW',
        icon: arrow_back,
      },
      {
        value: 'DOWN_ARROW',
        name: '↓',
        title: 'DOWN ARROW',
        icon: arrow_downward,
      },
      {
        value: 'UP_ARROW',
        name: '↑',
        title: 'UP ARROW',
        icon: arrow_upward,
      },
      {
        value: 'APPLICATION',
        name: '☰',
        title: 'Application: also known as the Menu key (Windows)',
        icon: application,
      },
      {
        value: 'LEFT_CONTROL',
        name: 'L-CTRL',
        title: 'Control modifier left of the spacebar',
      },
      {
        value: 'RIGHT_CONTROL',
        name: 'R-CTRL',
        title: 'Control modifier right of the spacebar',
      },
      {
        value: 'LEFT_SHIFT',
        name: 'L-Shift',
        title: 'Shift modifier left of the spacebar',
        // icon: shift,
      },
      {
        value: 'RIGHT_SHIFT',
        name: 'R-Shift',
        title: 'Shift modifier right of the spacebar',
        // icon: shift,
      },
      {
        value: 'WINDOWS',
        name: '❖',
        title: 'Labeled with a Windows logo on Windows keyboards',
        icon: windows,
      },
      {
        value: 'COMMAND',
        name: '⌘',
        title: 'Labeled as Command on Mac keyboards, with a clover glyph',
        icon: command,
      },
      {
        value: 'LEFT_ALT',
        name: '  L-ALT',
        title: 'Alt modifier left of the spacebar',
      },
      {
        value: 'RIGHT_ALT',
        name: 'R-ALT',
        title: 'Alt modifier right of the spacebar',
      },
      {
        value: 'ALT',
        name: '⌥',
        title: 'Option (Mac)',
        icon: macOption,
      },
    ],
  },
  {
    name: 'media',
    keys: [
      {
        value: 'BRIGHTNESS_DECREMENT',
        name: '☼',
        title: 'Decrease Brightnessn',
        icon: sunB,
      },
      {
        value: 'BRIGHTNESS_INCREMENT',
        name: '☀',
        title: 'Increase Brightness',
        icon: sunI,

      },
      {
        value: 'FAST_FORWARD',
        name: '▹▹',
        title: 'FAST FORWARD',
        icon: fastForward,
      },
      {
        value: 'REWIND',
        name: '◃◃',
        title: 'Rewind',
        icon: fastRewind,
      },
      {
        value: 'MUTE',
        name: '0',
        title: 'MUTE',
        icon: volumeOff,
      },
      {
        value: 'PLAY_PAUSE',
        name: '▷||',
        title: 'PLAY PAUSE',
        icon: playPause,
      },
      {
        value: 'SCAN_NEXT_TRACK',
        name: '▹▹|',
        title: 'Skip to next track',
        icon: skipNext,
      },
      {
        value: 'SCAN_PREVIOUS_TRACK',
        name: '|◁◁',
        title: 'Go back to previous track',
        icon: skipPrevious,
      },
      {
        value: 'STOP',
        name: '■',
        title: 'STOP',
        icon: stop,
      },
      {
        value: 'VOLUME_DECREMENT',
        name: 'VOL-',
        title: 'Decrease volume',
        icon: volumeDown,
      },
      {
        value: 'VOLUME_INCREMENT',
        name: 'VOL+',
        title: 'Increase volume',
        icon: volumeUp,
      },
    ],
  },
  {
    name: 'keybard controls',
    keys: [
      {
        value: 'SHOW_GAME',
        name: 'game',
        title: 'start game',
        icon: game,
      },
      {
        value: 'DISABLE_DISPLAY',
        name: 'display',
        title: 'disable display',
        icon: display,
      },
    ],
  },
]

export const FLATTERN_KEY_NAMES = KEY_NAMES.reduce((acc, group) => (
  [...acc, ...group.keys]
), typeCasting<IKey[]>([]))

export default KEY_NAMES
