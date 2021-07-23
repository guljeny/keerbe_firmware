import React, { memo, useState, useEffect, useCallback, useRef } from 'react'
import Key from 'components/Key'
import { TLayerName, TKey, TRow, TLayout } from 'types/layout'
import { LAYER_LIST, LAYOUT_DEFAULT } from 'constants/layout'
import typeCasting from 'utils/typeCasting'
import ButtonValueModal, { IModalActions } from 'components/ButtonValueModal'

import styles from './LayoutConstructor.m.scss'

interface IProps {
  layout: TLayout;
  activeLayer: TLayerName;
  setLayout: (value: TLayout | ((oldLayout: TLayout | null) => TLayout)) => void;
}

function LayoutConstructor ({ layout, activeLayer, setLayout }: IProps) {
  const buttonValueModalActions = useRef<IModalActions | null>(null)
  const [activeRow, setActiveRow] = useState<null | number>(null)
  const [activeKey, setActiveKey] = useState<null | number>(null)

  const setKeyValue = useCallback((newKey: TKey) => {
    if (activeRow === null || activeKey === null) return
    setLayout(oldLayout => typeCasting<TLayout>({
      ...(oldLayout || {}),
      [activeLayer]: (oldLayout ? oldLayout[activeLayer] : []).map(
        (row: TRow, rowIndex: number) => (
          row.map((key: TKey, keyIndex: number) => (
            keyIndex === activeKey && rowIndex === activeRow ? newKey : key
          ))
        ),
      ),
    }))
    buttonValueModalActions.current?.close()
  }, [setLayout, activeRow, activeKey, activeLayer])

  useEffect(() => {
    document.addEventListener('click', e => {
      if (!typeCasting<HTMLElement | null>(e.target)?.closest(`.${styles.key}`)) {
        buttonValueModalActions.current?.close()
        setActiveRow(null)
        setActiveKey(null)
      }
    })
  }, [])

  const onKeyClick = useCallback((e, rowIndex, keyIndex) => {
    setActiveRow(rowIndex)
    setActiveKey(keyIndex)
    buttonValueModalActions.current?.show(e.target)
  }, [setActiveKey, setActiveRow])

  const isButtonHasValue = activeRow !== null
    && activeKey !== null
    && !!layout[activeLayer][activeRow][activeKey]

  return (
    <div>
      {layout[activeLayer].map((row, rowIndex) => (
        <div className={styles.row} key={rowIndex}>
          {row.map((key, keyIndex) => {
            const defaultKey: TKey = layout[LAYOUT_DEFAULT][rowIndex][keyIndex]
            const isDefaultKeyLayout = !!defaultKey
              && activeLayer !== LAYOUT_DEFAULT
              && (LAYER_LIST as string[]).includes(defaultKey.value)
            return (
              <Key
                key={keyIndex}
                isActive={rowIndex === activeRow && keyIndex === activeKey}
                isDisabled={isDefaultKeyLayout}
                onClick={e => onKeyClick(e, rowIndex, keyIndex)}
                modifiers={styles.key}
                value={isDefaultKeyLayout ? defaultKey : key}
              />
            )
          })}
        </div>
      ))}
      <ButtonValueModal
        isLayerButtonVisible={activeLayer === LAYOUT_DEFAULT}
        isClearButtonVisible={isButtonHasValue}
        onClick={setKeyValue}
        actionsRef={buttonValueModalActions}
      />
    </div>
  )
}

export default memo(LayoutConstructor)
