export const generalConditions = [
  'Is',
  'Is not',
  'Contains',
  'Does not contain',
  'Starts with',
  'Ends with',
  'Is empty',
  'Is not empty',
] as const

export type GeneralConditions = (typeof generalConditions)[number]

export const keywordOperators = [
  'Exact match',
  'Include related',
  'Approximate match',
  'Expression',
  'Exclude'
] as const

export type KeywordOperators = (typeof keywordOperators)[number]

export const joinOperators = [
  'And',
  'Or'
] as const

export type JoinOperators = (typeof joinOperators)[number]
