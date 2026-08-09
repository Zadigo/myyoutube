import { mockNuxtImport, mountSuspended } from '@nuxt/test-utils/runtime'
import { describe, it, vi, expect } from 'vitest'
import VideoPage from '~/pages/videos/[id].vue'
import { videoDetailsFixture } from '~~/test/__fixtures__'
import { flushPromises } from '@vue/test-utils'

mockNuxtImport('useRoute', () => vi.fn().mockReturnValue({ params: { id: '123' } }))

mockNuxtImport('$fetch', () => vi.fn().mockResolvedValue(async () => videoDetailsFixture))

vi.mock('~/components/video/actions/Card.vue', () => ({
  default: defineComponent({
    template: '<div>Action Card</div>'
  })
}))

vi.mock('~/components/video/player/Overlay.vue', () => ({
  default: defineComponent({
    template: '<div data-testid="overlay"><slot /></div>'
  })
}))

vi.mock('~/components/video/Information.vue', () => ({
  default: defineComponent({
    template: '<div data-testid="information">Information</div>'
  })
}))

vi.mock('~/components/video/comment/Section.vue', () => ({
  default: defineComponent({
    template: '<div>Comment Section</div>'
  })
}))

vi.mock('~/components/video/UserRecommendations.vue', () => ({
  default: defineComponent({
    template: '<div data-testid="user-recommendations">User Recommendations</div>'
  })
}))

vi.mock('~/components/modals/Save.vue', () => ({
  default: defineComponent({
    template: '<div>Save Modal</div>'
  })
}))

vi.mock('~/components/modals/Report.vue', () => ({
  default: defineComponent({
    template: '<div>Report Modal</div>'
  })
}))

vi.mock('~/components/modals/Gift.vue', () => ({
  default: defineComponent({
    template: '<div>Gift Modal</div>'
  })
}))

vi.mock('~/components/modals/classification.vue', () => ({
  default: defineComponent({
    template: '<div>Classification Modal</div>'
  })
}))

vi.mock('~/components/modals/Donation.vue', () => ({
  default: defineComponent({
    template: '<div>Donation Modal</div>'
  })
}))

vi.mock('~/components/modals/Share.vue', () => ({
  default: defineComponent({
    template: '<div>Share Modal</div>'
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
          [IS_LOADING_SYMBOL]: ref(false),
          [CURRENT_VIDEO_SYMBOL]: ref(videoDetailsFixture)
        }
      }
    })

    await flushPromises()

    expect(component.find('[data-testid="comment-section"]').exists()).toBe(true)
    expect(component.find('[data-testid="user-recommendations"]').exists()).toBe(true)
  })
})
