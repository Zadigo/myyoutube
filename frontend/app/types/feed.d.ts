import type { DefaultMainCategories, DefaultSortBy, DefaultUploadDate, DefaultVideoLength } from '~/data'
import type { _DatabaseObject, Arrayable } from '.'
import type { CustomUser } from './accounts'


/**
 * @deprecated Use BaseVideo instead
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
 * @deprecated Use BaseVideo instead
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






export interface VideoTag extends _DatabaseObject {
    name: string
}

export type NestedChannelInfo = Pick<UserChannel, 'reference', 'name'> & {
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
