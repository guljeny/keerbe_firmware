import { FLATTERN_KEY_NAMES } from 'constants/keyNames'
import { LAYER_BUTTONS } from 'constants/layout'
import typeCasting from 'utils/typeCasting'
import { TLayout } from 'types/layout'

export default function (jsonLayout: string | { layout: TLayout }): TLayout | null {
  try {
    const layoutList: TLayout = typeof jsonLayout === 'string'
      ? JSON.parse(jsonLayout).layout
      : jsonLayout.layout
    return Object.entries(layoutList).reduce((acc, [layoutName, layout]) => ({
      ...acc,
      [layoutName]: layout.map(row => row.map(keyValue => {
        const baseValue = FLATTERN_KEY_NAMES.find(
          ({ value }) => value === typeCasting<string>(keyValue),
        )
        if (baseValue) return baseValue
        return LAYER_BUTTONS.find(({ value }) => value === typeCasting<string>(keyValue)) || null
      })),
    }), typeCasting<TLayout>({}))
  } catch (e) {
    return null
  }
}
