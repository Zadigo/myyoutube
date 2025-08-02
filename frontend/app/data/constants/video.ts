export const defaultVideoMenuActions = [
  'Store',
  'Download',
  'Save',
  'Gift',
  'Donate',
  'Share',
  'Recommendations',
  'Community note',
  'Classify',
  'Fact check',
  'Report'
] as const

export type DefaultVideoMenuActions = (typeof defaultVideoMenuActions)[number]
