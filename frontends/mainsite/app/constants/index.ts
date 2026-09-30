export * from './settings'

export const SOCIALS = [
  'Facebook',
  'X',
  'Instagram',
  'YouTube'
] as const

export type Socials = (typeof SOCIALS)[number] | (string & {})
