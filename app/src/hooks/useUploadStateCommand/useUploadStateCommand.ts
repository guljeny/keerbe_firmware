import { useMemo, useState, useCallback } from 'react'

interface IState {
  length: number;
  lastOperation: string | null;
  progress: number;
}

type TSetState = (v: string) => void

export function useUploadStateCommand (onEnd: () => void): [IState, TSetState] {
  const [uploadState, setUploadState] = useState<string[]>([])

  const state: IState = useMemo(() => {
    if (uploadState[uploadState.length - 1] === 'END') {
      onEnd && onEnd()
      setUploadState([])
      return { length: 0, lastOperation: null, progress: 0 }
    }
    const length = Number(uploadState[0]) || 0
    const lastOperation = uploadState.length > 0 ? uploadState[uploadState.length - 1] : null
    const progress = length ? (uploadState.length - 1) / length : 0
    return { length, lastOperation, progress }
  }, [uploadState, onEnd])

  const setState = useCallback((v: string) => {
    setUploadState(oldUploadState => [...oldUploadState, v.replace('\n', '')])
  }, [setUploadState])

  return [state, setState]
}

export default useUploadStateCommand
