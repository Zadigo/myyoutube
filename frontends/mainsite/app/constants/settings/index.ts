export const rankAs = [
  'Artist',
  'Business',
  'Sports commentator',
  'Athlete',
  'Public figure',
  'News publisher or broadcaster',
  'Content creator'
] as const

export type RankAs = (typeof rankAs)[number]

export const subscriptionTypes = [
  'Free',
  'YouTube+',
  'YouTube++'
] as const

export type SubscriptionType = (typeof subscriptionTypes)[number]


// Blocking

export const BLOCKING_DURATIONS = [
  'Forever',
  'For 24 hours',
  '7 days',
  '30 days'
] as const

export type BlockingDuration = (typeof BLOCKING_DURATIONS)[number]


// Ads

export const SENSITIVE_CATEGORIES = [
  'Alcohol',
  'Dating',
  'Gambling',
  'Pregnancy and parenting',
  'Weight loss'
] as const

export type SensitiveCategory = (typeof SENSITIVE_CATEGORIES)[number]
