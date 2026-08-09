import { describe, it, expect, vi, beforeEach } from 'vitest'
import { useViewingProfile } from '../../../app/composables'
import { mockNuxtImport } from '@nuxt/test-utils/runtime'

mockNuxtImport('useCookie', () => {
  return vi.fn((_name: string, _options: { sameSite: boolean; secure: boolean }) => {
    return {
      value: 'mocked-cookie-value'
    }
  })
})

describe('useViewingProfile', () => {
  it('should return the correct default values', () => {
    const result = useViewingProfile()
    expect(result).toBeDefined()
  })
})
