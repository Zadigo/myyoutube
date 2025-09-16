import type { _DatabaseObject } from '.'
import type { CustomUser } from './authentication'

export interface VideoTag extends _DatabaseObject {
    name: string
}

export type NestedChannelInfo = Pick<UserChannel, 'reference', 'name'> & {
    number_of_subscribers: number
    number_of_playlists: number
    channelplaylist_set: string[]
    tags: VideoTag[]
}

/**
 * @deprecated
 */
export interface VideosFeedResponseData extends _DatabaseObject {
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

/**
 * @deprecated
 */
export interface VideoInfo extends _DatabaseObject {
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
