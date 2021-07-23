import { TLayout } from 'types/layout'
import { LAYOUT_DEFAULT, LAYER_LIST } from 'constants/layout'

export default function (layout: TLayout) {
  return JSON.stringify({
    layout: (Object.entries(layout)).reduce((acc, [layerName, layer]) => ({
      ...acc,
      [layerName]: layer.map((row, rowIndex) => row.map((key, keyIndex) => {
        const defaultKey = layout[LAYOUT_DEFAULT][rowIndex][keyIndex]
        const isDefaultLayer = layerName === LAYOUT_DEFAULT
        const isLayoutKey = (LAYER_LIST as string[]).includes(defaultKey?.value || '')
        if (defaultKey?.value && !isDefaultLayer && isLayoutKey) {
          return defaultKey.value
        }
        return key?.value || ''
      })),
    }), {}),
  })
}
