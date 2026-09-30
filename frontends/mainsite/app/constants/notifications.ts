export const NOTIFICATION_TYPES = ['All', 'Messages', 'Uploads'] as const

export type NotificationType = (typeof NOTIFICATION_TYPES)[number]
