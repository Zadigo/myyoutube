import { describe, it, expect, vi } from 'vitest'
import { useFeedComposable, useSearchFeedComposable } from '../../../app/composables'
import { defineComponent } from 'vue'
import { mountSuspended } from '@nuxt/test-utils/runtime'
import type { NitroFetchOptions } from '#imports'

const mockFetch = vi.fn(async (url: string, options: NitroFetchOptions) => {
  if (url === '/api/videos' && options.method === 'GET') {
    return {
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
  }
  throw new Error(`Unexpected fetch call: ${url} with method ${options.method}`)
})

vi.stubGlobal('$fetch', mockFetch)

describe('useSearchFeedComposable', () => {
  it('should return the correct default values', () => {
    const result = useSearchFeedComposable()
    
    expect(result).toBeDefined()
    expect(result.search.value).toBe('')
    expect(result.category.value).toBe('All')
    expect(result.videoLength.value).toBe('4-20 minutes')
    expect(result.uploadDate.value).toBe('This week')
    expect(result.sortBy.value).toBe('Upload date')
  })

  it('should update the query values correctly', () => {
    const result = useSearchFeedComposable()

    result.search.value = 'test search'

    expect(result.search.value).toBe('test search')
  })
})

describe.todo('useFeedComposable', () => {
  it('should return the correct default values', async () => {
    let result: ReturnType<typeof useFeedComposable>

    const component = await mountSuspended(defineComponent({
      template: `
      <div>
        <span v-if="result.hasVideos" id="has-videos" />

        {{ result }}

        <article v-for="video in result.videos.allVideos.edges" :key="video.node.id" class="video">
          <h2>{{ video.node.title }}</h2>
          <p>{{ video.node.description }}</p>
        </article>
      </div>
      `,
      setup() {
        result = useFeedComposable()
        return {
          result
        }
      }
    }))

    console.log(component.html())

    expect(result).toBeDefined()
    expect(result.hasVideos.value).toBe(true)
    // expect(result.search.value).toBe('')
    // expect(result.category.value).toBe('All')
    // expect(result.videoLength.value).toBe('This week')
    // expect(result.uploadDate.value).toBe('This week')
    // expect(result.sortBy.value).toBe('Upload date')
  })
})
