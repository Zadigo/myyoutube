import type { Arrayable, ModerationReportSource } from '..'
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
  subjectCreatorId: string
  upvotes: number
  downvotes: number
  score: number
  status: CommunityNoteStatus
}

export type CommunityNote = BaseCommunityNote & { noteSources: Arrayable<ModerationReportSource> }

export type CommunityNoteNode = RelayNode<CommunityNote>

export type CommunityNotes = GraphQlData<'allnotes', RelayEdge<CommunityNote>>
