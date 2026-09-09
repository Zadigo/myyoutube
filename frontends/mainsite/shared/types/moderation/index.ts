export type * from './community_notes'
export type * from './fact_checking'

export interface ModerationReportSource {
  id: string
  url: string
  reference: string
  sourceCredibility: number
  updatedOn: string
  createdOn: string
}
