import React, { memo } from 'react'

import styles from './UploadingProgressModal.m.scss'

interface IProps {
  progress: number;
}

export function UploadingProgressModal ({ progress }: IProps) {
  return (
    <div className={styles.container}>
      <span className={styles.title}>Uploading</span>
      <div className={styles.progressBarContainer}>
        <div className={styles.progressBar} style={{ width: `calc(${progress}% - 4px)` }} />
      </div>
      <span className={styles.percent}>
        {progress.toFixed(1)}
        %
      </span>
    </div>
  )
}

export default memo(UploadingProgressModal)
