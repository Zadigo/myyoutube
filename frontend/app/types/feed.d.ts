import type { CustomUser } from './authentication'

export interface VideoTag {
    id: number
    name: string
}

export type NestedChannelInfo = Pick<UserChannel, 'reference', 'name'> & {
    number_of_subscribers: number
    number_of_playlists: number
    channelplaylist_set: string[]
    tags: VideoTag[]
}

export interface VideosFeedResponseData {
    id: number
    title: string
    description: string
    video_id: string
    user_channel: NestedChannelInfo,
    age_restricted: boolean
    user: CustomUser
    video: string
    channel_playlist: null
    created_on: string
}

export interface VideoInfo {
    id: number
    title: string
    video_id: string
    user_channel: NestedChannelInfo,
    user: CustomUser
    video: string
    channel_playlist: null
}
