import type { BaseCommunityNote } from '..'

export type BaseFactCheck = Pick<BaseCommunityNote, 'id' | 'reference' | 'createdOn' | 'author' | 'updatedOn'> & {
  videoId: string
}
