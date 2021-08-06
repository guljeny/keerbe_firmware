import React, { memo, useState, useEffect, useCallback, useContext } from 'react'
import classnames from 'classnames'
import { prepareLaout, layoutToJson, jsonToLayout } from 'utils/layout'
import Header from 'components/Header'
import { LAYOUT_DEFAULT } from 'constants/layout'
import { TLayerName, TLayout } from 'types/layout'
import LayoutConstructor from 'components/LayoutConstructor'
import UploadingProgressModal from 'components/UploadingProgressModal'
import runProcess from 'utils/runProcess'
import { KeyboardContext, LayoutContext } from 'constants/context'
import scanKeyboardService from 'utils/scanKeyboardService'
import useUploadStateCommand from 'hooks/useUploadStateCommand'
import typeCasting from 'utils/typeCasting'
import defaultLayout from '../../../../firmware/layout.json'

import styles from './LayoutBuilder.m.scss'

function LayoutBuilder () {
  const { serial, setSerial, type, initialLayout, clearInitialLayout } = useContext(KeyboardContext)
  const [uploadState, setUploadState] = useUploadStateCommand(scanKeyboardService.run)
  const [updateState, setUpdateState] = useUploadStateCommand(scanKeyboardService.run)
  const [layout, setLayout] = useState<TLayout | null>(null)
  const [activeLayer, setActiveLayer] = useState<TLayerName>(LAYOUT_DEFAULT)

  const setInitialLayout = useCallback(() => {
    initialLayout && setLayout(initialLayout)
  }, [setLayout, initialLayout])

  const setEmptyLayout = useCallback(() => {
    setLayout(prepareLaout(type))
  }, [setLayout, type])

  const setDefaultLayout = useCallback(() => {
    setLayout(jsonToLayout(typeCasting<{layout: TLayout}>(defaultLayout)))
  }, [setLayout])

  const exportLayout = useCallback(() => {
    if (!serial || !layout) return
    scanKeyboardService.stop()
    const jsonLayout = layoutToJson(layout)
    runProcess('upload_layout', [serial, jsonLayout], setUploadState)
  }, [serial, layout, setUploadState])

  const reset = useCallback(() => {
    if (!serial) return
    scanKeyboardService.stop()
    setSerial(null)
    clearInitialLayout()
    setDefaultLayout()
    runProcess('reset_memory', [serial], data => {
      if (data === 'END') {
        scanKeyboardService.run()
      }
    })
  }, [serial, setSerial, clearInitialLayout, setDefaultLayout])

  const update = useCallback(() => {
    if (!serial) return
    scanKeyboardService.stop()
    runProcess('update', [serial], setUpdateState)
  }, [serial, setUpdateState])

  useEffect(() => {
    if (!layout) setInitialLayout()
  }, [layout, initialLayout, setInitialLayout])

  return (
    <LayoutContext.Provider
      value={{ setDefaultLayout, setEmptyLayout, setInitialLayout, reset, update }}
    >
      <section
        className={classnames(styles.layoutBuilder, type, updateState.length && styles.blurred)}
      >
        <Header
          onExportClick={exportLayout}
          isLoading={!!uploadState.length}
          activeLayer={activeLayer}
          setActiveLayer={setActiveLayer}
        />
        <div className={styles.layoutContainer}>
          {layout && (
            <LayoutConstructor layout={layout} activeLayer={activeLayer} setLayout={setLayout} />
          )}
        </div>
      </section>
      {!!updateState.length && <UploadingProgressModal progress={updateState.progress * 100} />}
    </LayoutContext.Provider>
  )
}

export default memo(LayoutBuilder)
