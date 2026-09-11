import type { BaseCommunityNote } from '..'

export type BaseFactCheck = Pick<BaseCommunityNote, 'id' | 'reference' | 'createdOn' | 'author' | 'updatedOn'> & {
  videoId: string
}

export type SourceDetails = {
  start_time: string
  end_time: string
  explanation: string
  article_sources: string[]
}
