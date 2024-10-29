import { CustomUser } from "./authentication"

export interface VideosFeedResponseData {
    id: number
    title: string
    description: string
    video_id: string
    user_channel: {
        number: number
        reference: string
        name: string
        number_of_subscribers: number
        number_of_playlists: number
        channelplaylist_set: string[]
        tags: string[]
    },
    age_restricted: boolean
    user: CustomUser
    video: string
    channel_playlist: null
    created_on: string
}

export interface Video {
    id: number
    title: string
    video_id: string
    user_channel: {
        id: number
        reference: string
        name: string
        number_of_subscribers: number
        number_of_playlists: number
        channelplaylist_set: []
        tags: []
    },
    user: CustomUser
    video: string
    channel_playlist: null
}
