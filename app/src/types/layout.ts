export type TLayoutName = 'KEEBEE_1'
export type TLayerName = 'DEFAULT' | 'LAYOUT_1' | 'LAYOUT_2'

export interface IKey {
  value: string | TLayerName;
  name: string;
  title?: string;
  icon?: string;
}

export interface IKeyCombination {
  combination: string[];
  command: string;
}

export type TKey = IKey | null

export type TRow = TKey[]

export type TLayer = TRow[]

export type TLayout = Record<TLayerName, TLayer>
