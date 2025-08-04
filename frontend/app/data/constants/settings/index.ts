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
