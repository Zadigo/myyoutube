import type { MenuItem } from 'primevue/menuitem'
import type { RouteParamsGeneric } from 'vue-router'
import type { DefaultVideoMenuActions } from '~/data/constants/video'

export type * from './accounts'
export type * from './channels'
export type * from './comments'
export type * from './fact_checking'
export type * from './feed'
export type * from './notifications'
export type * from './playlist'
export type * from './settings'
export type * from './settings/notifications'
export type * from './studio'
export type * from './video'

export type Nullable<T> = T | null

export type Undefineable<T> = T | undefined

export type Maybe<T> = T | null | undefined

export type Arrayable<T> = T[] | readonly T[]

export type Refeable<T> = Ref<Undefineable<T>> | Ref<Arrayable<T | undefined>>

/**
 * @deprecated Use GraphQlResponse instead
 */
export interface _DatabaseObject { id: number }

/**
 * @deprecated Use GraphQlResponse instead
 */
export interface _DatabaseDataTimes { create_on: string, update_on: string }

export interface ExtendedRouteParamsGeneric extends RouteParamsGeneric {
  id: string
}

/**
 * @deprecated Use GraphQlResponse instead
 */
export interface ApiResponse<T> {
  next: number
  previous: number
  results: T[]
}

export interface VideoMenuItem extends MenuItem {
  label?: DefaultVideoMenuActions
}

export interface SessionCache {
  categories: Arrayable<string>
}



export type InterfaceKeys<I> = keyof I & string 

export type NullableTypes<T> = {
  [P in keyof T]?: Nullable<T[P]>
}

export type GraphQlResponse<T extends string, R = Record<string, unknown>> = {
  data: {
    [key in T]: {
      edges: Array<{ node: R }>
    }
  }
}

export type GraphQlSingleResponse<T extends string, R = Record<string, unknown>> = {
  data: {
    [key in T]: R
  }
}

export type GraphQlEdges<T> = { edges: Array<{ node: T }> }

export interface GraphQlPaginationInfo {
  pageInfo: {
    startCursor: string
    endCursor: string
    hasNextPage: boolean
    hasPreviousPage: boolean
  }
}
