import React, { memo, MouseEvent } from 'react'
import classnames from 'classnames'
import KeyValue from 'components/KeyValue'
import { TKey } from 'types/layout'

import styles from './Key.m.scss'

interface IProps {
  isActive?: boolean;
  isDisabled?: boolean;
  value: TKey;
  onClick: (e: MouseEvent<HTMLButtonElement>) => void;
  modifiers?: string;
}

export function Key ({ isActive, isDisabled, onClick, value, modifiers }: IProps) {
  return (
    <button
      type='button'
      className={classnames(
        styles.key,
        isActive && styles.active,
        isDisabled && styles.disabled,
        modifiers,
      )}
      onClick={onClick}
    >
      {value && <KeyValue {...value} />}
    </button>
  )
}

export default memo(Key)
