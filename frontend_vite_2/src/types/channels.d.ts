export interface UserChannel {
    reference: string
    user: {
        id: number
        firstname: string
        lastname: string
    }
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
