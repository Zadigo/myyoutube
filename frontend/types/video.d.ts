interface PlaylistUserChannel {
    id: number
    reference: string
    name: string
    number_of_subscribers: number
    number_of_playlists: number
    channelplaylist_set: string[]
    tags: {
        id: number
        name: string
    }[]
}

export interface Playlist {
    id: number
    title: string
    description: string
    video_id: string
    user_channel: PlaylistUserChannel
    age_restricted: boolean
    video: string
    channel_playlist: string
    user: {
        id: number
        firstname: string
        lastname: string
        username: string
        get_full_name: string
    },
    created_on: string
}
