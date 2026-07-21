import { describe, expect, it } from 'vitest'
import { useCreateCommentComposable } from '../../../../app/composables'

describe('useCreateCommentComposable', () => {
  it('should return an object with the expected properties', async () => {
    const result = useCreateCommentComposable()

    expect(result).toHaveProperty('newComment')
    expect(result).toHaveProperty('create')
    expect(result).toHaveProperty('reply')

    expect(result.create).toBeInstanceOf(Function)
    expect(result.reply).toBeInstanceOf(Function)

    expect(result.newComment.value).toEqual('')
  })
})
