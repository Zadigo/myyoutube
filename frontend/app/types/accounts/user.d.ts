import type { Nullable, NullableTypes } from ".."

export type BaseUserProfile = {
	id: string
	avatar: string
	birthdate: string
	createdOn: string
	isProfessional: boolean
} & NullableTypes<{
  address: string
  telephone: string
  zipCode: string
  city: string
  customerId: string
}>

export interface BaseUser {
	id: string
	email: string
	firstname?: Nullable<string>
	lastname?: Nullable<string>
	isActive: boolean
	isAdmin: boolean
	isStaff: boolean
	isSuperuser: boolean
	lastLogin: string
	password: string
	username: string
}
