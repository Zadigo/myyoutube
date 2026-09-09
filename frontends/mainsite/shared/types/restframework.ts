
/**
 * @deprecated Use GraphQlResponse instead
 */
export interface _DatabaseObject { id: number }

/**
 * @deprecated Use GraphQlResponse instead
 */
export interface _DatabaseDataTimes { create_on: string, update_on: string }

/**
 * @deprecated Use GraphQlResponse instead
 */
export interface ApiResponse<T> {
  next: number
  previous: number
  results: T[]
}
