import React from 'react'
import { IKeyboardContext } from 'types/keyboardContext'
import { ILayoutContext } from 'types/layoutContext'

export const KeyboardContext = React.createContext<IKeyboardContext>({
  setSerial: () => {},
  clearInitialLayout: () => {},
  serial: null,
  type: null,
  initialLayout: null,
})

export const LayoutContext = React.createContext<ILayoutContext>({
  setDefaultLayout: () => {},
  setEmptyLayout: () => {},
  setInitialLayout: () => {},
  reset: () => {},
  update: () => {},
})
