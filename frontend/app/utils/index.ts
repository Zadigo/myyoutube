export function inProduction() {
  // console.log(process.env.NODE_ENV)
  // return import.meta.env.MODE !== 'development'
  return process.env.NODE_ENV !== 'development'
}

export function scrollToTop() {
  window.scroll({ top: 0, behavior: 'smooth' })
}

export function isNull<T>(item: T): boolean {
  let trueValue

  if (isRef(item)) {
    trueValue = item.value
  } else {
    trueValue = item
  }

  return (
    trueValue === null ||
    typeof trueValue === 'undefined' ||
    trueValue === '' ||
    trueValue === ' '
  )
}
