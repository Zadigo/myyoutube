import { mountSuspended } from '@nuxt/test-utils/runtime'
import { describe, it, expect, vi } from 'vitest'
import BaseAsyncFeed from '~/components/BaseAsyncFeed.vue'
import type { Feed } from '~/types'
import { definedTestCases } from '~~/test/__mocks__'

const { useFeedComposable } = vi.hoisted(() => {
  const useFeedComposable = vi.fn(() => {    
    return {
      videos: ref([]),
      hasVideos: ref(false)
    }
  })
  return { useFeedComposable }
})

vi.mock('~/composables/use/feed.ts', async (original) => {
  const actual = await original<typeof import('~/composables/use/feed.ts')>()
  return {
    ...actual,
    useFeedComposable
  }
})

describe('components > BaseAsyncFeed', () => {
  const testCases = definedTestCases((manager) => {
    return manager.parameterize(
      [
        {
          title: 'with videos',
          expectedValue: []
        },
        {
          title: 'without videos',
          expectedValue: []
        }
      ]
    )
  })

  testCases.runner.forEach((testCase) => {
    it(`should render BaseAsyncFeed component ${testCase.title}`, async () => {
      useFeedComposable.mockReturnValue({
        videos: ref<Feed>(testCase.expectedValue || [] as Feed),
        hasVideos: ref(false)
      })
      const component = await mountSuspended(BaseAsyncFeed)
      
    })  
  })
})
