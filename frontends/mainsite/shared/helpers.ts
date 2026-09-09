// import { toBaseProduct } from './utils'

/**
 * Filters products based on a search query.
 * @param query 
 */
export function filterFunc(query: string | undefined) {
  return (video: BaseVideo) => {
    // const item = toBaseProduct(product)

    if (!video) return false
    if (!query) return true
    
    return (
      video.title.toLocaleLowerCase().includes(query.toLocaleLowerCase()) ||
      video.description.toLocaleLowerCase().includes(query.toLocaleLowerCase())
    )
  }
}
