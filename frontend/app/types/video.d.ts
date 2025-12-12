import type { Nullable } from '.'

export interface VideoTechnicalDetails {
  currentTime: number
  formattedCurrentTime: string
  wasPlayed: boolean
  percentagePlayed: number
  playPauseCount: number
}

export interface BaseVideo {
	id: string
	active: boolean
	category: string
	ageRestricted: boolean
	commentStrategy: string
	description: string
	createdOn: string
	duration: number
	framerate: number
	height: number
	modifiedOn: string
	ratingsAreVisible: boolean
	recordingDate: string
	recordingLanguage: string
	recordingLocation?: Nullable<string>
	title: string
	video: string
	videoId: string
	visibility: string
	views: number
	width: number
}
