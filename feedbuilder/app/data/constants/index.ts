import type { BlockNames } from "~/types"

export const duration = [
    '30 minutes',
    '3 hours',
    '12 hours',
    '24 hours',
    '3 days',
    '7 days'
]

export const sourceNames = [
    'Entire network',
    'Tags',
    'Single user',
    'List',
    'Feed',
    'Single post',
    'Labels'
]

export const blocks: BlockNames[] = [
    'Source',
    'Remove',
    'RegExp',
    'Replace',
    'Sort',
    'Limit'
]
