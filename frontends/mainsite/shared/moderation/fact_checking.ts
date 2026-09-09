import type { Arrayable, BaseCommunityNote, ModerationReportSource } from '..'
import type { GraphQlData, RelayEdge, RelayNode } from '../graphql'

export type CommunityNoteStatus = 'DRAFT' | 'PENDING' | 'APPROVED' | 'REJECTED' | 'FLAGGED'

export type BaseFactChck = Pick<BaseCommunityNote, 'id' | 'reference' | 'createdOn' | 'author' | 'updatedOn'> & {
  videoId: string
}

export type CommunityNote = BaseCommunityNote & { factcheckSources: Arrayable<ModerationReportSource> }

export type CommunityNoteNode = RelayNode<CommunityNote>

export type CommunityNotes = GraphQlData<'allnotes', RelayEdge<CommunityNote>>
