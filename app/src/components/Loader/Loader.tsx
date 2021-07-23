import React, { memo } from 'react'
import classNames from 'classnames'

import styles from './Loader.m.scss'

interface IProps {
  size?: number;
  modifiers?: string;
}

function Loader ({ size = 30, modifiers }: IProps) {
  const sizeInPx = `${size}px`
  return (
    <div
      style={{ width: sizeInPx, height: sizeInPx }}
      className={classNames(styles.loader, modifiers)}
    />
  )
}

export default memo(Loader)
