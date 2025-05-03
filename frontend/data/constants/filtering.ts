export const defaultSortBy = [
  'Upload date',
  'View count',
  'Rating'
] as const

export type DefaultSortBy = (typeof defaultSortBy)[number]

export const defaultVideoLength = [
  'Under 4 minutes',
  '4-20 minutes',
  'Over 20 minutes'
] as const

export type DefaultVideoLength = (typeof defaultVideoLength)[number]

export const defaultUploadDate = [
  'Last hour',
  'Today',
  'This week',
  'This month',
  'This year'
] as const

export type DefaultUploadDate = (typeof defaultUploadDate)[number]
