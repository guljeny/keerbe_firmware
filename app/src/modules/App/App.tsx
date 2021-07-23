import React, { memo, useMemo, useEffect, useState } from 'react'
import LayoutBuilder from 'modules/LayoutBuilder'
import KeyboardScanScreen from 'components/KeyboardScanScreen'
import runProcess from 'utils/runProcess'
import { KeyboardContext } from 'constants/context'
import scanKeyboardService from 'utils/scanKeyboardService'
import { LAYOUT_CONFIG } from 'constants/layout'
import { jsonToLayout } from 'utils/layout'
import { TLayout, TLayoutName } from 'types/layout'

function App () {
  const [serial, setSerial] = useState<string | null>(null)
  const [type, setType] = useState<TLayoutName | null>(null)
  const [initialLayout, setInititalLayout] = useState<TLayout | null>(null)
  useEffect(() => {
    scanKeyboardService.run(v => {
      try {
        const data = JSON.parse(v)
        setSerial(data.serial)
        LAYOUT_CONFIG[data.type] && setType(data.type)
      } catch (err) {
        setSerial(null)
        setType(null)
      }
    })
  }, [])

  useEffect(() => {
    if (type && serial && !initialLayout) {
      runProcess('get_layout', [serial], (jsonLayout: string) => {
        try {
          setInititalLayout(jsonToLayout(jsonLayout))
        } catch (e) {}
      })
    }
  }, [serial, initialLayout, setInititalLayout, type])

  const contextValue = useMemo(() => ({
    serial,
    type,
    initialLayout,
    setSerial,
    clearInitialLayout: () => setInititalLayout(null),
  }), [serial, initialLayout, type, setSerial, setInititalLayout])

  return (
    <KeyboardContext.Provider value={contextValue}>
      <KeyboardScanScreen />
      {type && <LayoutBuilder />}
    </KeyboardContext.Provider>
  )
}

export default memo(App)
