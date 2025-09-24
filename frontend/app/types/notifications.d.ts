import type { _DatabaseObject, ApiResponse } from '.'

export interface Notification extends _DatabaseObject {
  text: string
}

export type NotificationApiResponse = ApiResponse<Notification>
