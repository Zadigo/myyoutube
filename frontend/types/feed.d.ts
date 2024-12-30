import type { CustomUser } from "./authentication"
import type { NestedChannelInfo } from "./channels"

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
