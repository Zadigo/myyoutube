import { mockNuxtImport, mountSuspended } from '@nuxt/test-utils/runtime'
import { describe, it, expect, vi } from 'vitest'
import Playlists from '~/pages/playlists.vue'

mockNuxtImport('$fetch', () => vi.fn().mockReturnValue(() => Promise.resolve({ data: { results: [] } })))

vi.mock('~/components/playlists/Details.vue', () => ({
  default: defineComponent({
    template: '<div>Details</div>'
  })
}))

vi.mock('~/components/playlists/List.vue', () => ({
  default: defineComponent({
    template: '<div>List</div>'
  })
}))

describe('pages > playlists', () => {
  it('should render playlists page', async () => {
    const component = await mountSuspended(Playlists)
  })
})
