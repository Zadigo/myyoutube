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
  'Report',
  'Classify'
] as const

export type DefaultVideoMenuActions = (typeof defaultVideoMenuActions)[number]

export const subscriptionModes = [
  'All',
  'None'
] as const

export type SubscriptionModes = (typeof subscriptionModes)[number]
