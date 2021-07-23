import React, { useContext, useState, useEffect } from 'react'
import classnames from 'classnames'
import { KeyboardContext, LayoutContext } from 'constants/context'
import typeCasting from 'utils/typeCasting'
import menuIcon from 'images/icons/menu.svg'

import styles from './Menu.m.scss'

export default function Menu () {
  const [isOpened, setIsOpened] = useState(false)
  const { type } = useContext(KeyboardContext)
  const {
    setDefaultLayout, setEmptyLayout,
    setInitialLayout, reset, update,
  } = useContext(LayoutContext)

  useEffect(() => {
    document.addEventListener('click', e => {
      if (!typeCasting<HTMLElement | null>(e.target)?.closest(`.${styles.menu}`)) {
        setIsOpened(false)
      }
    })
  }, [])

  return (
    <div className={styles.menu}>
      <button
        type='button'
        dangerouslySetInnerHTML={{ __html: menuIcon }}
        onClick={() => setIsOpened(oldIsOpened => !oldIsOpened)}
      />
      <div className={classnames(styles.dropout, isOpened && styles.visible)}>
        <div className={styles.title}>{type || ''}</div>
        <ul onClick={() => setIsOpened(false)}>
          <li>
            <span>Layout</span>
            <ul>
              <li onClick={setInitialLayout}>Use from keyboard</li>
              <li onClick={setDefaultLayout}>Use default</li>
              <li onClick={setEmptyLayout}>Clear</li>
            </ul>
          </li>
          <li>
            <span>Keyboard</span>
            <ul>
              <li onClick={reset}>Reset</li>
              <li onClick={update}>Update</li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  )
}
