import { describe, expect, it } from 'vitest'
import { useCommentsComposable } from '../../../../app/composables'

describe('useCommentsComposable', () => {
  it('should return an object with the expected properties', async () => {
    const result = await useCommentsComposable()

    expect(result).toHaveProperty('comments')
    expect(result).toHaveProperty('pinnedComments')
    expect(result).toHaveProperty('unpinnedComments')
    expect(result).toHaveProperty('sortCommentsBy')
  })
})
