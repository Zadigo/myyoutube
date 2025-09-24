import type { _DatabaseObject } from '.'
import type { BaseUser } from './accounts'

export interface VideoComment extends _DatabaseObject {
    user: BaseUser
    content: string
    from_creator: boolean
    pinned: boolean
    is_liked: boolean
    is_disliked: boolean
    number_of_replies: number
    user_channel: string
    created_on: string
}
