import type { _DatabaseObject } from './restframework'
import type { Socials } from '~/constants'

export interface Categories extends _DatabaseObject {
    title: string
}

export interface Subcategories extends Categories {
    id: number
}

export type VideoInfo = Pick<BaseVideo, 'id' | 'title' | 'description'>

export type NewVideoRequestData = {
    title: string
    description: string
    tags: string[]
    category: number | null
    subcategory: number | null
    files: File[]
    has_paid_promotion: boolean
    publication: {
        language: string
        publication_time: string // ISO 8601 format
        publication_date: string // ISO 8601 format
        recording_location: string
    }
    channel_playlist: number | null
    teaser: File | null
    visibility: {
        public: boolean
        subscribers_only: boolean
        is_premiere: boolean
        panelize: boolean
        age_restricted: boolean
    }
    monetization: {
        ads: boolean
        gifts: boolean
    }
    participants: {
        fullname: string
        url: string
        handle: Socials
    }[]
}
