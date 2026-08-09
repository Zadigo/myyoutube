import type { MenuItem } from 'primevue/menuitem'

export const DEFAULT_SORT_BY = [
  'Upload date',
  'View count',
  'Rating'
] as const

export type DefaultSortBy = (typeof DEFAULT_SORT_BY)[number]

export interface DefaultSortByMenuItem extends MenuItem {
  label: DefaultSortBy
}

export const DEFAULT_VIDEO_LENGTH = [
  'Under 4 minutes',
  '4-20 minutes',
  'Over 20 minutes'
] as const

export type DefaultVideoLength = (typeof DEFAULT_VIDEO_LENGTH)[number]

export const DEFAULT_UPLOAD_DATE = [
  'Last hour',
  'Today',
  'This week',
  'This month',
  'This year'
] as const

export type DefaultUploadDate = (typeof DEFAULT_UPLOAD_DATE)[number]
