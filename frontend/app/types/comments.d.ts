export interface VideoComment {
    id: number
    user: {
        id: number
        firstname: string | null
        lastname: string | null
        username: string
        get_full_name: string
    },
    content: string
    from_creator: boolean
    pinned: boolean
    is_liked: boolean
    is_disliked: boolean
    number_of_replies: number
    user_channel: string
    created_on: string
}
