import type { CustomUser } from "./authentication"

export interface UserChannel {
    reference: string
    user: CustomUser
    name: string
    description: string
    banner: string
    resized_banner: string
    channel_thumbnail: string
    category: string
    email: string
    instagram: string
    tiktok: string
    facebook: string
    subscribers: []
    is_verified: boolean
    created_on: string
}

export interface NestedChannelInfo {
    id: number
    reference: string
    name: string
    number_of_subscribers: number
    number_of_playlists: number
    channelplaylist_set: string[]
    tags: string[]
}
