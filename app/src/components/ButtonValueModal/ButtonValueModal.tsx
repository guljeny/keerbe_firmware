import React, { Fragment, useCallback, useState, useEffect, useRef, memo } from 'react'
import classnames from 'classnames'
import keyNames from 'constants/keyNames'
import KeyValue from 'components/KeyValue'
import { LAYER_BUTTONS, LAYOUT_DEFAULT } from 'constants/layout'
import { TKey } from 'types/layout'

import styles from './ButtonValueModal.m.scss'

const distance = 20

export interface IModalActions {
  show: (target: HTMLDivElement) => void;
  close: () => void;
}

interface IProps {
  onClick: (newKey: TKey) => void;
  isLayerButtonVisible?: boolean;
  isClearButtonVisible?: boolean;
  actionsRef: { current: IModalActions | null };
}

function ButtonValueModal (props: IProps) {
  const { actionsRef, onClick, isLayerButtonVisible, isClearButtonVisible } = props
  const modalEl = useRef<HTMLDivElement>(null)

  const [position, setPosition] = useState({ x: window.innerWidth / 2, y: 0 })
  const [isVisible, setIsVisible] = useState(false)

  const close = useCallback(() => {
    setIsVisible(false)
  }, [setIsVisible])

  const updatePosition = useCallback((target: HTMLDivElement) => {
    const targetRect = target?.getBoundingClientRect()
    const modalRect = modalEl?.current?.getBoundingClientRect()
    let x = targetRect.left + targetRect.width + distance
    let y = targetRect.top
    if (x + targetRect.width + (modalRect?.width || 0) + distance > window.innerWidth) {
      x = targetRect.left - (modalRect?.width || 0) - distance
    }
    if (y + targetRect.height + (modalRect?.height || 0) > window.innerHeight) {
      y = window.innerHeight - (modalRect?.height || 0) - distance
    }
    setPosition({ x, y })
  }, [setPosition, modalEl])

  const show = useCallback((target: HTMLDivElement) => {
    updatePosition(target)
    setIsVisible(true)
  }, [setIsVisible, updatePosition])

  useEffect(() => {
    if (actionsRef) actionsRef.current = { show, close }
  }, [actionsRef, close, show])

  return (
    <div
      className={classnames(styles.buttonValueModal, isVisible && styles.visible)}
      style={{
        left: `${position.x}px`,
        top: `${position.y}px`,
      }}
      ref={modalEl}
      onClick={e => e.stopPropagation()}
    >
      {isClearButtonVisible && (
        <div
          className={styles.button}
          onClick={() => {
            onClick(null)
          }}
        >
          <KeyValue name='Clear' value='' />
        </div>
      )}
      {isLayerButtonVisible && (
        <>
          <span className={styles.title}>Layer</span>
          {LAYER_BUTTONS.map(key => {
            if (key.value === LAYOUT_DEFAULT) return null
            return (
              <div
                key={key.value}
                className={styles.button}
                onClick={() => {
                  onClick(key)
                }}
              >
                <KeyValue {...key} />
              </div>
            )
          })}
        </>
      )}
      {keyNames.map(({ name, keys }) => (
        <Fragment key={name}>
          <span className={styles.title}>{name}</span>
          {keys.map(key => (
            <div
              key={key.value}
              className={styles.button}
              onClick={() => {
                onClick(key)
              }}
            >
              <KeyValue {...key} />
              {key.title && <span className={styles.tooltip}>{key.title}</span>}
            </div>
          ))}
        </Fragment>
      ))}
    </div>
  )
}

export default memo(ButtonValueModal)
