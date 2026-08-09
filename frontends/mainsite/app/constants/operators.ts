export const GENERAL_CONDITIONS = [
  'Is',
  'Is not',
  'Contains',
  'Does not contain',
  'Starts with',
  'Ends with',
  'Is empty',
  'Is not empty',
] as const

export type GeneralConditions = (typeof GENERAL_CONDITIONS)[number]

export const KEYWORD_OPERATORS = [
  'Exact match',
  'Include related',
  'Approximate match',
  'Expression',
  'Exclude'
] as const

export type KeywordOperators = (typeof KEYWORD_OPERATORS)[number]

export const JOIN_OPERATORS = [
  'And',
  'Or'
] as const

export type JoinOperators = (typeof JOIN_OPERATORS)[number]
