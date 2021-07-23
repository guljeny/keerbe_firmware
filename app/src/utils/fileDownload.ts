export default function (content: string, name: string = 'layout.json') {
  const a = document.createElement('a')
  const file = new Blob([content], { type: 'text/plain' })
  a.href = URL.createObjectURL(file)

  a.download = name
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
}
