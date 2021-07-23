import { useRef, useEffect } from 'react'

export default function useMouned () {
  const componentIsMounted = useRef(true)
  useEffect(() => () => { componentIsMounted.current = false }, [])
  return () => componentIsMounted.current
}
