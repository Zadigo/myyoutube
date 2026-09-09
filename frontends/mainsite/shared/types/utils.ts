import type { Ref } from 'vue'

export type Nullable<T> = T | null

export type Undefineable<T> = T | undefined

export type Maybe<T> = T | Nullable<T> | Undefineable<T>

export type Arrayable<T> = T[] | readonly T[]

export type Refeable<T> = Ref<Undefineable<T>> | Ref<Arrayable<T | undefined>>

export type InterfaceKeys<I> = keyof I & string

export type NullableTypes<T> = { [ P in keyof T ]?: Nullable<T[ P ]> }
