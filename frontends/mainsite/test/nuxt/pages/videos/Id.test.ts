import { mockNuxtImport, mountSuspended } from '@nuxt/test-utils/runtime'
import { describe, it, vi, expect } from 'vitest'
import { ref } from 'vue' // Ensure ref is imported for your global provide
import VideoPage from '~/pages/videos/[id].vue'
import { videoDetailsFixture } from '~~/test/__fixtures__'
import { flushPromises } from '@vue/test-utils'

// Fix 1: Properly mock useRoute
mockNuxtImport('useRoute', () => vi.fn().mockReturnValue({ params: { id: '123' } }))

// Fix 2: Directly resolve to the data fixture object, not a function
mockNuxtImport('$fetch', () => vi.fn().mockResolvedValue(async () => videoDetailsFixture))

// Fix 3: Handle hoisting by creating a standard component object structure
vi.mock('~/components/video/comment/Section.vue', () => ({
  default: {
    name: 'MockedCommentSection',
    template: '<div data-testid="comment-section">Comment Section</div>'
  }
}))

vi.mock('~/components/video/UserRecommendations.vue', () => ({
  default: {
    name: 'MockedRecommendations',
    template: '<div data-testid="user-recommendations">User Recommendations</div>'
  }
}))

// Fix the rest of your mocks using the object template format
vi.mock('~/components/video/actions/Card.vue', () => ({ default: { template: '<div>Action Card</div>' } }))
vi.mock('~/components/video/player/Overlay.vue', () => ({ default: { template: '<div data-testid="overlay"><slot /></div>' } }))
vi.mock('~/components/video/Information.vue', () => ({ default: { template: '<div data-testid="information">Information</div>' } }))
vi.mock('~/components/modals/Save.vue', () => ({ default: { template: '<div>Save Modal</div>' } }))
vi.mock('~/components/modals/Report.vue', () => ({ default: { template: '<div>Report Modal</div>' } }))
vi.mock('~/components/modals/Gift.vue', () => ({ default: { template: '<div>Gift Modal</div>' } }))
vi.mock('~/components/modals/classification.vue', () => ({ default: { template: '<div>Classification Modal</div>' } }))
vi.mock('~/components/modals/Donation.vue', () => ({ default: { template: '<div>Donation Modal</div>' } }))
vi.mock('~/components/modals/Share.vue', () => ({ default: { template: '<div>Share Modal</div>' } }))
vi.mock('~/app/components/video/player/Base.vue', () => ({ default: { template: '<div>Base Player</div>' } }))

describe.todo('pages > videos/[id]', () => {
  it('should render video page and mocked async components', async () => {
    // mountSuspended handles Suspense and initial setup automatically
    const wrapper = await mountSuspended(VideoPage, {
      global: {
        provide: {
          [ IS_LOADING_SYMBOL ]: ref(false),
          [ CURRENT_VIDEO_SYMBOL ]: ref(videoDetailsFixture)
        }
      }
    })
    console.log(wrapper.html()) // Debugging: Check the rendered HTML

    // Force Vue's defineAsyncComponent loaders to cycle and resolve to your mocks
    await flushPromises()

    // Assert your mocked async components are mounted cleanly
    expect(wrapper.find('[data-testid="comment-section"]').exists()).toBe(true)
    expect(wrapper.find('[data-testid="user-recommendations"]').exists()).toBe(true)
  })
})
