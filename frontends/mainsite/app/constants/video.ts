export const DEFAULT_VIDEO_MENU_ACTIONS = [
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

export type DefaultVideoMenuActions = (typeof DEFAULT_VIDEO_MENU_ACTIONS)[number]

export const SUBSCRIPTION_MODES = [
  'All',
  'None'
] as const

export type SubscriptionModes = (typeof SUBSCRIPTION_MODES)[number]
