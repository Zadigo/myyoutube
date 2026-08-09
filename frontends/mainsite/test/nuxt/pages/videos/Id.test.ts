import { mockNuxtImport, mountSuspended } from '@nuxt/test-utils/runtime'
import { describe, it, vi } from 'vitest'
import VideoPage from '~/pages/videos/[id].vue'
import { videoDetailsFixture } from '~~/test/__fixtures__'

mockNuxtImport('useRoute', () => vi.fn().mockReturnValue({ params: { id: '123' } }))

mockNuxtImport('$fetch', () => vi.fn().mockResolvedValue(async () => videoDetailsFixture))

vi.mock('~/components/video/comment/Section.vue', () => ({
  default: defineComponent({
    template: '<div>Comment Section</div>'
  })
}))

vi.mock('~/components/video/UserRecommendations.vue', () => ({
  default: defineComponent({
    template: '<div>User Recommendations</div>'
  })
}))

vi.mock('~/components/modals/Save.vue', () => ({
  default: defineComponent({
    template: '<div>Save Modal</div>'
  })
}))

vi.mock('~/components/modals/Report.vue', () => ({
  default: defineComponent({
    template: '<div>Save Modal</div>'
  })
}))

vi.mock('~/components/modals/Gift.vue', () => ({
  default: defineComponent({
    template: '<div>Save Modal</div>'
  })
}))

vi.mock('~/components/modals/classification.vue', () => ({
  default: defineComponent({
    template: '<div>Save Modal</div>'
  })
}))

vi.mock('~/components/modals/Donation.vue', () => ({
  default: defineComponent({
    template: '<div>Save Modal</div>'
  })
}))

vi.mock('~/components/modals/Share.vue', () => ({
  default: defineComponent({
    template: '<div>Save Modal</div>'
  })
}))

vi.mock('~/app/components/video/player/Base.vue', () => ({
  default: defineComponent({
    template: '<div>Base Player</div>'
  })
}))

describe.only('pages > videos/[id]', () => {
  it('should render video page', async () => {
    const component = await mountSuspended(VideoPage, {
      global: {
        provide: {
          isLoading: ref(false),
          currentVideo: ref(videoDetailsFixture)
        }
      }
    })
  })
})
