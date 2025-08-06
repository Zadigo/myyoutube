export interface SourceOptions {
    duration: '30 minutes' | '3 hours' | '12 hours' | '24 hours' | '3 days' | '7 days'
    source: 'Entire network' | 'Tags' | 'Single user' | 'List' | 'Feed' | 'Single post' | 'Labels'
}

export interface RegexOptions {
    pattern: string
    source: 'Video transcript' | 'Video title' | 'Video description'
    invert: boolean
    case_sensitive: boolean
}

export interface SortOptions {
    by: 'Creation date' | 'Like count' | 'Reply count' | 'Random'
    direction: 'Ascending' | 'Descending'
}

export interface RequestData {
    sources: SourceOptions[]
    regex: RegexOptions[],
    sorting: SortOptions[]
}

export type BlockNames = 'Source' | 'Remove' | 'RegExp' | 'Replace' | 'Sort' | 'Limit'

export interface CreatedComponent {
    position: number
    component: Component,
    data: SourceOptions | RegexOptions | SortOptions
}

export interface CustomUser {
    id: number
    firstname: string
    lastname: string
    get_full_name: string
}

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

export interface VideoItem {
    id: number
    title: string
    description: string
    video_id: string
    user_channel: UserChannel
    user: CustomUser
    created_on: string
}
