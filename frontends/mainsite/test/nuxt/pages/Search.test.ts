import { mountSuspended } from '@nuxt/test-utils/runtime'
import { describe, it } from 'vitest'
import Search from '~/pages/search.vue'

describe('pages > search', () => {
  it('should render search page', async () => {
    const component = await mountSuspended(Search)
  })
})
