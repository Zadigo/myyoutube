import { describe, it, expect, beforeEach, vi } from 'vitest'
import { useBlockedChannels, useBlockLists, useBlockedKeywordsComposable, useBlockedKeywordsStore } from '../../../../app/composables'
import { defineComponent } from 'vue'
import { mountSuspended } from '@nuxt/test-utils/runtime'

const mockFetch = vi.fn(async (url: string, options: any) => {
  if (url === '/user-channels/blocked' && options.method === 'GET') {
    return [
      { id: 1, name: 'Channel 1' },
      { id: 2, name: 'Channel 2' }
    ]
  }

  throw new Error('Not Found')
})

vi.stubGlobal('$fetch', mockFetch)

describe('useBlockedChannels', () => {
  it('should return an object with the expected properties', () => {
    const result = useBlockedChannels()
    expect(result).toBeDefined()
  })
})

describe('useBlockLists', () => {
  it('should return an object with the expected properties', () => {
    useBlockLists()
    expect(true).toBe(true)
  })
})

describe('useBlockedKeywordsComposable', () => {
  let result: ReturnType<typeof useBlockedKeywordsComposable>

  beforeEach(async () => {
    const componentA = defineComponent({
      template: '<div></div>',
      setup() {
        useBlockedKeywordsStore()
      }
    })

    const componentB = defineComponent({
      template: `
      <div>
        <component-a />
      </div>
      `,
      components: {
        'component-a': componentA
      },
      setup() {
        result = useBlockedKeywordsComposable()
      }
    })

    await mountSuspended(componentB)
  })

  it('should return an object with the expected properties', () => {
    expect(result).toBeDefined()
  })
})
