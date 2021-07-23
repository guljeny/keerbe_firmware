import React, { memo } from 'react'
import { IKey } from 'types/layout'

import styles from './KeyValue.m.scss'

export function KeyValue ({ name, icon }: IKey) {
  if (icon) return <span className={styles.image} dangerouslySetInnerHTML={{ __html: icon }} />
  if (name) return <span className={styles.text}>{name}</span>
  return null
}

export default memo(KeyValue)
