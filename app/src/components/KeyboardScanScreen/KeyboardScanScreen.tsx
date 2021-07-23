import React, { useState, useContext, useCallback, useEffect, useRef } from 'react'
import Loader from 'components/Loader'
import Button from 'components/buttons/Button'
import { KeyboardContext } from 'constants/context'
import runProcess from 'utils/runProcess'

import styles from './KeyboardScanScreen.m.scss'

export default function KeyboardScanScreen () {
  const [isButtonVisible, setIsButtonVisible] = useState(false)
  const { serial, type, initialLayout } = useContext(KeyboardContext)
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null)

  const onRestore = useCallback(() => {
    setIsButtonVisible(false)
    const process = runProcess('flash')
    process.on('exit', () => { timerRef.current = null })
  }, [])

  useEffect(() => {
    if (!serial || !type || !initialLayout) {
      if (!timerRef.current) {
        timerRef.current = setTimeout(() => setIsButtonVisible(true), 10000)
      }
    } else {
      setIsButtonVisible(false)
      timerRef.current && clearTimeout(timerRef.current)
      timerRef.current = null
    }
    return () => {
      timerRef.current && clearTimeout(timerRef.current)
      timerRef.current = null
    }
  // This effect logic dependent of timer id
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [serial, type, initialLayout, timerRef.current])

  if (serial && type && initialLayout) return null

  return (
    <div className={styles.container}>
      <Loader />
      {isButtonVisible && <Button modifiers={styles.button} onClick={onRestore}>Restore</Button>}
    </div>
  )
}
