export * from './numbers'

export function inProduction() {
  // console.log(process.env.NODE_ENV)
  // return import.meta.env.MODE !== 'development'
  return process.env.NODE_ENV !== 'development'
}

export function scrollToTop() {
  window.scroll({ top: 0, behavior: 'smooth' })
}
