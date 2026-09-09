import type { _DatabaseObject } from '.'

export interface Categories extends _DatabaseObject {
    title: string
}

export interface Subcategories extends Categories {
    id: number
}

// export interface FileUploadRequestData {
//     video: File | null
//     title: string | null
//     description: string | null
//     channel_playlist: string | null
//     recording_location: string | null
//     visibility: boolean
//     category: string | null
//     subcategory: string | null
//     age_restricted: boolean
// }
