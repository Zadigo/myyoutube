import { describe, it, expect, vi, beforeEach } from 'vitest'
import { useFeedComposable, useSearchFeedComposable } from '../../../app/composables'
import { computed, defineComponent, ref } from 'vue'
import { mockNuxtImport, mountSuspended } from '@nuxt/test-utils/runtime'
import type { Feed } from '../../../app/types'
import type { NitroFetchOptions, AsyncDataExecuteOptions } from '#imports'
import { isDefined } from '@vueuse/core'

const responseData: Feed = {
  allVideos: {
    edges: [
      {
        node: {
          id: '1',
          title: 'Video 1',
          description: 'Description for Video 1',
          category: 'Category 1',
          videoLength: '10 minutes',
          uploadDate: '2024-01-01',
        },
      },
      {
        node: {
          id: '2',
          title: 'Video 2',
          description: 'Description for Video 2',
          category: 'Category 2',
          videoLength: '15 minutes',
          uploadDate: '2024-02-01',
        },
      },
    ],
  },
}

const mockFetch = vi.fn(async (url: string, options: NitroFetchOptions) => {
  if (url === '/api/videos' && options.method === 'GET') {
    return responseData
  }
  throw new Error(`Unexpected fetch call: ${url} with method ${options.method}`)
})

vi.stubGlobal('$fetch', mockFetch)

mockNuxtImport('useFetch', () => {
  return (_url: string, _options: NitroFetchOptions) => {
    return {
      data: ref<Feed>(responseData),
      execute: vi.fn(async (_options: AsyncDataExecuteOptions<Feed>) => {
        return responseData
      }),
    }
  }
})

vi.mock('@vueuse/core', async (original) => {
  const actual = await original<typeof import('@vueuse/core')>()
  return {
    ...actual,
    computedAsync: vi.fn((_fn) => {
      // return computed(() => responseData)
      return ref(responseData)
    }),
  }
})

describe.todo('useSearchFeedComposable', () => {
  let result: unknown

  beforeEach(async () => {
    await mountSuspended(defineComponent({
      template: '<div></div>',
      async setup() {
        result = await useSearchFeedComposable()
        return {
          result
        }
      }
    }))
  })

  it('should return the correct default values', async () => {    
    expect(result).toBeDefined()
    if (isDefined(result)) {
      expect(result.search.value).toBe('')
      expect(result.category.value).toBe('All')
      expect(result.videoLength.value).toBe('4-20 minutes')
      expect(result.uploadDate.value).toBe('This week')
      expect(result.sortBy.value).toBe('Upload date')
    }
  })

  it('should update the query values correctly', () => {
    expect(result).toBeDefined()
    if (isDefined(result)) {
      result.search.value = 'test search'
      expect(result.search.value).toBe('test search')
    }
  })
})

describe.todo('useFeedComposable', () => {
  it('should return the correct default values', async () => {
    let result: ReturnType<typeof useFeedComposable>

    await mountSuspended(defineComponent({
      template: `
      <div>
        <span v-if="result.hasVideos" id="has-videos" />

        <div v-if="result.videos">
          <article v-for="video in result.videos.value.allVideos.edges" :key="video.node.id" class="video">
            <h2>{{ video.node.title }}</h2>
            <p>{{ video.node.description }}</p>
          </article>
        </div>
      </div>
      `,
      setup() {
        result = useFeedComposable()
        return {
          result
        }
      }
    }))

    expect(result).toBeDefined()
    expect(result.hasVideos.value).toBe(true)
  })
})
