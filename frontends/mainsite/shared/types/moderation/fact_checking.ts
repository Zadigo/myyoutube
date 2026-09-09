import type { BaseCommunityNote } from '..'

export type CommunityNoteStatus = 'DRAFT' | 'PENDING' | 'APPROVED' | 'REJECTED' | 'FLAGGED'

export type BaseFactCheck = Pick<BaseCommunityNote, 'id' | 'reference' | 'createdOn' | 'author' | 'updatedOn'> & {
  videoId: string
}
