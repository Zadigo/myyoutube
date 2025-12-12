import type { DefaultMainCategories, DefaultSortBy, DefaultUploadDate, DefaultVideoLength } from '~/data'
import type { _DatabaseObject, Arrayable, UserChannel } from '.'
import type { CustomUser } from './accounts'



// type NullableTypes<T> = {
//   [P in keyof T]?: Nullable<T[P]>
// }


// export type Userprofile = {
// 	id: string
// 	avatar: string
// 	customerId?: Nullable<string>
// 	birthdate: string
// 	telephone?: Nullable<string>
// 	address?: Nullable<string>
// 	city?: Nullable<string>
// 	zipCode?: Nullable<string>
// 	isProfessional: string
// 	createdOn: string
// } & NullableTypes<{ google: string }>

// export interface User {
// 	id: string
// 	username: string
// 	email: string
// 	firstname?: Nullable<string>
// 	lastname?: Nullable<string>
// 	userprofile: Userprofile
// }

// export interface RootObject {
// 	id: string
// 	videoId: string
// 	title: string
// 	description: string
// 	duration: number
// 	category: string
// 	ageRestricted: boolean
// 	recordingDate: string
// 	recordingLocation?: Nullable<string>
// 	recordingLanguage: string
// 	ratingsAreVisible: boolean
// 	video: string
// 	user: User
// 	width: number
// 	height: number
// 	framerate: number
// 	views: number
// 	modifiedOn: string
// 	createdOn: string
// }


export interface VideoTag extends _DatabaseObject {
  name: string
}

export type NestedChannelInfo = Pick<UserChannel, 'reference' | 'name'> & {
  number_of_subscribers: number
  number_of_playlists: number
  channelplaylist_set: Arrayable<string>
  tags: Arrayable<VideoTag>
}

export interface SearchQuery {
  search?: string
  category?: DefaultMainCategories
  videoLength?: DefaultVideoLength
  uploadDate?: DefaultUploadDate
  sortBy?: DefaultSortBy
}

export interface BaseVideo extends _DatabaseObject {
  title: string
  description: string
  video_id: string
  user_channel: NestedChannelInfo,
  user: CustomUser
  age_restricted: boolean
  video: string
  channel_playlist: null
  created_on: string
}
