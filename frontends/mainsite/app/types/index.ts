import type { MenuItem } from 'primevue/menuitem'
import type { RouteParamsGeneric } from 'vue-router'
import type { DefaultVideoMenuActions } from '~/constants/video'
import type { Arrayable } from '#shared/utils'

export type * from './restframework'

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
