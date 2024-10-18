export interface VideosFeedResponseData {
    id: number
    title: string
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
    video: string
    channel_playlist: null
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
    video: string
    channel_playlist: null
}
