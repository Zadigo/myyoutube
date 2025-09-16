import type { _DatabaseObject, Arrayable, BaseUser, Nullable } from '.'

interface SimpleTag extends _DatabaseObject {
    name: string
}

interface SimpleUserChannel extends _DatabaseObject {
    reference: string
    name: string
    number_of_subscribers: number
    number_of_playlists: number
    channelplaylist_set: string[]
    tags: Arrayable<SimpleTag>
}

export interface PlaylistVideo extends _DatabaseObject {
    title: string
    description: string
    video_id: string
    user_channel: SimpleUserChannel
    age_restricted: boolean
    video: string
    channel_playlist: Nullable<string>
    user: BaseUser
    created_on: string
}

export interface Playlist {
    id: number
    name: string
    description: Nullable<string>
    videos: PlaylistVideo[]
    visibility: string
    created_on: string
}
