import React, { memo } from 'react'
import classNames from 'classnames'
import { Button } from 'components/buttons'
import Menu from 'components/Menu'
import { TLayerName } from 'types/layout'
import { LAYER_BUTTONS } from 'constants/layout'

import styles from './Header.m.scss'

interface IProps {
  activeLayer: TLayerName;
  setActiveLayer: (layout: TLayerName) => void;
  onExportClick: () => void;
  isLoading?: boolean;
}

function Header ({ activeLayer, setActiveLayer, onExportClick, isLoading }: IProps) {
  return (
    <header className={classNames(styles.header)}>
      <Menu />
      <ul className={styles.layoutList}>
        {LAYER_BUTTONS.map(({ name, value }) => (
          <li
            key={value}
            className={classNames(value === activeLayer && styles.active, styles.layoutButton)}
            onClick={() => setActiveLayer(value)}
          >
            {name}
          </li>
        ))}
      </ul>
      <Button onClick={onExportClick} isLoading={isLoading}>Apply</Button>
    </header>
  )
}

export default memo(Header)
