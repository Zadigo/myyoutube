export interface VideoComment {
    id: number
    user: {
        id: number
        firstname: string
        lastname: string
    },
    content: string
    from_creator: boolean
    pinned: boolean
    number_of_replies: number
    created_on: string
}
