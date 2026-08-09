import { mountSuspended } from '@nuxt/test-utils/runtime'
import { describe, it, expect, vi } from 'vitest'
import Index from '~/pages/index.vue'

vi.mock('~/components/BaseAsyncFeed.vue', () => ({
  default: defineAsyncComponent({
    loader: async () => defineComponent({
      template: '<div>BaseAsyncFeed</div>'
    })
  })
}))

vi.mock('~/composables/use/feed.ts', async (original) => {
  const actual = await original<typeof import('~/composables/use/feed.ts')>()
  return {
    ...actual,
    useFeedComposable: vi.fn(() => ({
      hasVideos: ref(true),
      videos: ref([])
    }))
  }
})

describe('pages > index', () => {
  it('render index page', async () => {
    const component = await mountSuspended(Index)
    // console.log(component.html())
  })
})
