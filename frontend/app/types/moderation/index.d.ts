import type { _DatabaseObject, ApiResponse } from '..'

export interface CommunityNote extends _DatabaseObject {
  author: string
}

export type CommunityNoteApiResponse = ApiResponse<CommunityNote>
