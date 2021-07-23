export default function date (initialValue?: string | number | Date) {
  const currentDate = new Date(initialValue || Date.now())
  return {
    addHour (count: number = 1) {
      return date(currentDate.setHours(currentDate.getHours() + count))
    },
    get utcHours () {
      return currentDate.getUTCHours()
    },
    get utcMinutes () {
      return currentDate.getUTCMinutes()
    },
    get utcSeconds () {
      return currentDate.getUTCSeconds()
    },
    get timestamp () {
      return currentDate.getTime()
    },
    get localeTime () {
      return currentDate.toLocaleTimeString()
    },
    get localeDate () {
      return currentDate.toLocaleDateString()
    },
    get toNow () {
      return (currentDate.getTime() - date().timestamp) + currentDate.getTimezoneOffset() / 60
    },
  }
}
