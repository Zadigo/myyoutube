import type { MenuItem } from 'primevue/menuitem'
import type { RouteParamsGeneric } from 'vue-router'
import type { DefaultVideoMenuActions } from '~/data/constants/video'

export type * from './accounts'
export type * from './channels'
export type * from './comments'
export type * from './fact_checking'
export type * from './feed'
export type * from './graphql'
export type * from './notifications'
export type * from './playlist'
export type * from './restframework'
export type * from './settings'
export type * from './settings/notifications'
export type * from './studio'
export type * from './video'

export type Nullable<T> = T | null

export type Undefineable<T> = T | undefined

export type Maybe<T> = T | Nullable<T> | Undefineable<T>

export type Arrayable<T> = T[] | readonly T[]

export type Refeable<T> = Ref<Undefineable<T>> | Ref<Arrayable<T | undefined>>

export type InterfaceKeys<I> = keyof I & string 

export type NullableTypes<T> = { [P in keyof T]?: Nullable<T[P]> }

// Other Types

export interface ExtendedRouteParamsGeneric extends RouteParamsGeneric {
  id: string
}

export interface VideoMenuItem extends MenuItem {
  label?: DefaultVideoMenuActions
}

export interface SessionCache {
  categories: Arrayable<string>
}

export type VisilityStatus = 'Public' | 'Private'
