import { TLayoutName, TLayout } from 'types/layout'

export interface IKeyboardContext {
  serial: string | null;
  type: TLayoutName | null;
  setSerial: (v: string | null) => void;
  clearInitialLayout: () => void;
  initialLayout: TLayout | null;
}
