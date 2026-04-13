// import type { BlockNames } from "~/types"

export const duration = [
    '30 minutes',
    '3 hours',
    '12 hours',
    '24 hours',
    '3 days',
    '7 days'
] as const

export type Duration = (typeof duration)[number]

export const sourceNames = [
    'Entire network',
    'Tags',
    'Single user',
    'List',
    'Feed',
    'Single post',
    'Labels'
] as const

export type SourceNames = (typeof sourceNames)[number]

export const blockNames = [
    'Source',
    'Remove',
    'RegExp',
    'Replace',
    'Sort',
    'Limit'
] as const

export type BlockNames = (typeof blockNames)[number]

export const sortBy = [
  'Creation date',
  'Like count',
  'Reply count',
  'Random'
] as const

export type SortBy = (typeof sortBy)[number]

export const sortDirection = ['Ascending', 'Descending'] as const

export type SortDirection = (typeof sortDirection)[number]
