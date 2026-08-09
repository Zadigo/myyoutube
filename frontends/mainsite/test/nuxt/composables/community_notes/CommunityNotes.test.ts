import { describe, expect, it } from 'vitest'
import { useCommunityNotesComposable, useCommunityNoteById } from '../../../../app/composables'
import type { CommunityNoteNode } from '../../../../app/types'
import { faker } from '@faker-js/faker'

describe('useCommunityNotesComposable', () => {
  it('should return an object with the expected properties', async () => {
    const result = await useCommunityNotesComposable()

    expect(result).toHaveProperty('communityNotes')
    expect(result).toHaveProperty('search')
    expect(result).toHaveProperty('searchedCommunityNotes')
  })
})

const node: CommunityNoteNode = {
  node: {
    id: '1',
    reference: 'ref-1',
    author: {
      id: 'author-1',
      username: 'user1'
    },
    title: 'Note Title',
    description: 'Note Description',
    createdOn: new Date().toISOString(),
    creatorId: 'creator-1',
    downvotes: faker.number.int({ min: 0, max: 100 }),
    upvotes: faker.number.int({ min: 0, max: 100 }),
    noteSources: [],
    score: 8,
    status: 'APPROVED',
    subjectCreatorId: 'subject-creator-1',
  }
}

describe('useCommunityNoteById', () => {
  it('should return an object with the expected properties', async () => {
    const result = useCommunityNoteById(node)

    expect(result).toHaveProperty('approval')
    expect(result).toHaveProperty('shouldDemandReason')
    expect(result).toHaveProperty('reason')
    expect(result).toHaveProperty('toggleShouldDemandReason')
    expect(result).toHaveProperty('createVote')

    expect(result.toggleShouldDemandReason).toBeInstanceOf(Function)
    expect(result.createVote).toBeInstanceOf(Function)
  })
})
