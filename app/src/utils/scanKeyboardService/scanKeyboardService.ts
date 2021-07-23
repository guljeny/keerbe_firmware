import runProcess from 'utils/runProcess'

class ScanKeyboardService {
  /* eslint-disable no-underscore-dangle */
  __process = null

  __callback: ((data: string) => void) | null = null

  __timer: ReturnType<typeof setTimeout> | null = null

  run = (cb?: (v: string) => void) => {
    if (cb) this.__callback = cb
    if (!this.__callback) return
    if (this.__timer) this.stop()
    this.__timer = setTimeout(() => {
      runProcess('scan', [], (data: string) => {
        this.__callback && this.__callback(data)
        this.run()
      })
    }, 1000)
  }

  stop = () => {
    if (this.__timer) clearTimeout(this.__timer)
  }
  /* eslint-enable no-underscore-dangle */
}

const scanKeyboardService = new ScanKeyboardService()

window.onbeforeunload = () => {
  scanKeyboardService.stop()
}

export default scanKeyboardService
