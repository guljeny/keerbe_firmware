import React, { memo } from 'react'
import Loader from 'components/Loader'
import classNames from 'classnames'

import styles from './Button.m.scss'
import modifiersStyles from './ButtonModifiers.m.scss'

interface IProps {
  children?: React.ReactNode;
  onClick?: () => void;
  isLoading?: boolean;
  type?: 'button' | 'reset' | 'submit';
  modifiers?: string;
}

function Button ({ children, isLoading, modifiers, ...restProps }: IProps) {
  return (
    <button
      type='button'
      className={classNames(styles.button, isLoading && modifiersStyles.disabled, modifiers)}
      {...restProps}
    >
      {children}
      {isLoading && (
        <div className={styles.loaderContainer}>
          <Loader size={20} />
        </div>
      )}
    </button>
  )
}

export default memo(Button)
