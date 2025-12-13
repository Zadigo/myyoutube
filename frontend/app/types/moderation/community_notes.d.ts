import type { Arrayable } from '..'
import type { GraphQlData, RelayEdge, RelayNode } from '../graphql'

export type CommunityNoteStatus = 'DRAFT' | 'PENDING' | 'APPROVED' | 'REJECTED' | 'FLAGGED'

export interface BaseCommunityNote {
  id: string
  reference: string
  title: string
  description: string
  author: {
    id: string
    username: string
  }
  createdOn: string
  creatorId: string
  upvotes: number
  downvotes: number
  score: number
  status: CommunityNoteStatus
}

export interface CommunityNoteSource {
  id: string
  url: string
  reference: string
  sourceCredibility: number
  updatedOn: string
  createdOn: string
}

export type CommunityNote = BaseCommunityNote & { noteSources: Arrayable<CommunityNoteSource> }

export type CommunityNoteNode = RelayNode<CommunityNote>

export type CommunityNotes = GraphQlData<'allnotes', RelayEdge<CommunityNote>>
