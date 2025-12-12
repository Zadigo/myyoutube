import type { BaseUserChannel, GraphQlData, Nullable, RelayEdge, VisilityStatus, BaseVideo, RelayNode } from '.'

type BasePlaylist = {
  id: string
  playlistId: string
  isIntelligent: boolean
  name: string
  description: Nullable<string>
  visibility: VisilityStatus
  createdOn: string
}

type UserChannel = Pick<BaseUserChannel, 'id' | 'reference' | 'name'>

export type PlaylistVideo = Pick<BaseVideo, 'id' | 'title' | 'description' | 'videoId'> & { userChannel: UserChannel }

export type PlaylistVideoNode = RelayNode<PlaylistVideo>

export type PlaylistVideos = RelayEdge<PlaylistVideo>

export type SinglePlaylist = BasePlaylist & { videos: PlaylistVideos }

export type Playlist = GraphQlData<'allplaylists', RelayEdge<SinglePlaylist>>
