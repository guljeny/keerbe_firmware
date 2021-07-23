import { TLayoutName, TLayerName } from 'types/layout'

export const LAYOUT_DEFAULT = 'DEFAULT'
export const LAYOUT_1 = 'LAYOUT_1'
export const LAYOUT_2 = 'LAYOUT_2'

export const LAYER_LIST: TLayerName[] = [LAYOUT_DEFAULT, LAYOUT_1, LAYOUT_2]
export const LAYER_BUTTONS = LAYER_LIST.map((layout, index) => ({
  value: layout,
  name: index ? `Layer ${index}` : 'Default',
}))

export const LAYOUT_CONFIG: Record<TLayoutName, number[]> = {
  KEEBEE_1: [12, 12, 12, 12],
}
