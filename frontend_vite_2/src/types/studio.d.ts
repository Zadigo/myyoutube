export interface Categories {
    title: string
}

export interface Subcategories {
    title: string
}

export interface FileUploadRequestData {
    video: File | null
    title: string | null
    description: string | null
    channel_playlist: string | null
    recording_location: string | null
    visibility: boolean
    category: string | null
    subcategory: string | null
}
