import type { _DatabaseObject } from '..'

export * from './authentication'
export * from './user'


export type BaseUser = _DatabaseObject & {
  firstname: string
  lastname: string
  username: string
  get_full_name: string
}
