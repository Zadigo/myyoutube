import { faker } from '@faker-js/faker'
import { computed, ref, toValue } from 'vue'
import videoFixtures from '~~/public/fixtures/videos.json'
import { filterFunc } from '#shared/helpers'
import type { H3Event } from 'h3'
import { getRouterParam } from 'h3'
import { getQuery } from 'h3'
 
/**
 * Utility functions for loading and manipulating video fixtures for testing purposes.
 */
export function useLoadFixtures<T extends BaseVideo = BaseVideo>() {
  const fixtures = computed(() => videoFixtures)

  function getItem(event: H3Event) {
    const id = getRouterParam(event, 'id')

    if (!id) return undefined
    return fixtures.value.find((video) => video.id.toString() === id)
  }

  function raw() {
    return toValue(fixtures)
  }

  function singleItem() {
    return raw().at(0) as T | undefined
  }
  
  function search(event: H3Event) {
    const query = getQuery<{ q: string }>(event)
    return fixtures.value.filter(filterFunc(query.q))
  }

  function filter(options: ProductFilterOptions) {
    return fixtures.value.filter((video) => {
      const size = options.sizes || []
      // const material = options.materials || []

      const sizeMatch = size.length === 0 || video.sizeSet.some((s) => size.includes(s.name))
      // const materialMatch = material.length === 0 || material.includes(product.material)

      // return sizeMatch && materialMatch
      return sizeMatch
    })
  }

  function toNodes(values: T[] | undefined): VideoNode[] {
    if (!values) return []
    return values.map((video) => ({
      node: video
    }))
  }

  function toPaginated(values: T[]) {
    return {
      edges: toNodes(values),
    }
  }

  return {
    /**
     * Returns the computed array of video fixtures loaded from the JSON file. 
     * This can be used to access the entire set of videos for testing or 
     * demonstration purposes.
     */
    fixtures,
    /**
     * Retrieves a specific video from the loaded 
     * fixtures based on the 'id' parameter in the event.
     */
    getItem,
    /**
     * Returns the first video from the loaded fixtures, 
     * which can be useful for testing or demonstration purposes.
     */
    singleItem,
    /**
     * Returns the raw array of loaded fixtures without any filtering or transformation.
     */
    raw,
    /**
     * Filters the loaded video fixtures based on a search query extracted from the event's parameters.
     * @param event - The H3Event from which to extract the search query.
     */
    search,
    /**
     * Converts an array of videos into a structure that mimics the Relay pagination format.
     */
    toNodes,
    /**
     * Simulates the graphene pagination structure by 
     * converting an array of videos into a paginated format which
     * relies on Relay specifications.
     */
    toPaginated,
    /**
     * Filters the loaded video fixtures based on the provided sizes and materials.
     * @param options - An object containing optional arrays of sizes and materials to filter by.
     */
    filter
  }
}

/**
 * Utility function for loading a collection fixture for testing purposes.
 */
export function useLoadCollectionFixture() {
  /**
   * Returns a reactive reference to a collection fixture, 
   * which includes a randomly generated name and the loaded
   *  product fixtures.
   */
  const result = ref<CollectionProducts>({
    data: {
      collection: {
        name: faker.word.words({ count: { min: 2, max: 5 } }),
        products: toValue(useLoadFixtures().fixtures)
      }
    }
  })

  return result
}

export function useLoadSearchCollectionFixture() {
  const result = useLoadCollectionFixture()
  const { toNodes } = useLoadFixtures()

  return computed(() => {
    return {
      data: {
        searchCollection: {
          edges: toNodes(result.value.data.collection.products)
        }
      }
    }
  })
}

export function useFirebaseSessionCollectionFixture() {
  const template = ref<SessionData>({
    cart: {
      items: [],
      total: 0,
      numberOfItems: 0,
      paymentIntent: null,
      status: 'active',
      viewCount: 0
    },
    language: { choice: 'en', selected: false },
    recommendations: [],
    searchHistory: []
  })
  return template
}
