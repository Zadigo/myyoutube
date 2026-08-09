import { mockNuxtImport, mountSuspended } from '@nuxt/test-utils/runtime'
import { describe, it, expect, vi } from 'vitest'
import Notifications from '~/pages/notifications.vue'

mockNuxtImport('$fetch', () => vi.fn().mockReturnValue(() => Promise.resolve({ data: { results: [] } })))

describe('pages > notifications', () => {
  it('should render notifications page', async () => {
    const component = await mountSuspended(Notifications)
  })
})
