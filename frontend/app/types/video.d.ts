export interface VideoTechnicalDetails {
  currentTime: number
  formattedCurrentTime: string
  wasPlayed: boolean
  percentagePlayed: number
  playPauseCount: number
}

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

// export interface BaseVideo {
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

