import { LAYOUT_CONFIG, LAYER_LIST } from 'constants/layout'
import { TLayoutName, TLayout } from 'types/layout'
import typeCasting from 'utils/typeCasting'
import prepareLayer from './prepareLayer'

export default function (type: TLayoutName | null): TLayout {
  if (!type) {
    return LAYER_LIST.reduce((acc, layerName) => (
      { ...acc, [layerName]: [] }
    ), typeCasting<TLayout>({}))
  }
  const layerConfig = LAYOUT_CONFIG[type]
  return LAYER_LIST.reduce((acc, layerName) => ({
    ...acc,
    [layerName]: prepareLayer(layerConfig),
  }), typeCasting<TLayout>({}))
}
