import type { MenuItem } from 'primevue/menuitem'
import type { RouteParamsGeneric } from 'vue-router'
import type { DefaultVideoMenuActions } from '~/data/constants/video'

export * from './accounts'
export * from './channels'
export * from './comments'
export * from './feed'
export * from './video'
export * from './studio'
export * from './settings/notifications'
export * from './settings'
export * from './playlist'
export * from './fact_checking'

export interface VideoMenuItem extends MenuItem {
  label?: DefaultVideoMenuActions
}

export interface SessionCache {
  categories: []
}

export interface ExtendedRouteParamsGeneric extends RouteParamsGeneric {
  id: string
}
