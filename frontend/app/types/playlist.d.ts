import type { BaseUserChannel, GraphQlEdges, Nullable, VisilityStatus } from "."

type Videos = GraphQlEdges<Pick<BaseVideo, 'id'>>

type UserChannel = Pick<BaseUserChannel, 'id' | 'name'>

type _Playlist = {
    id: string
    playlistId: string
    isIntelligent: boolean
    name: string
    description: Nullable<string>
    visibility: VisilityStatus
    createdOn: string   
} 

export type Playlist = _Playlist & { videos: Videos } & { userChannel: UserChannel }
