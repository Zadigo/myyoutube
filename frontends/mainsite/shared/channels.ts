import type { Arrayable, BaseUser, RelayNode } from '.'

export interface Tag {
  id: string
  name: string
}

export type Subscriber = RelayNode<Pick<BaseUser, 'id' | 'username'>>

export interface ChannelPlaylistSet {
  id: string
  name: string
  createdOn: string
  videoSet: RelayNode<BaseVideo>
}

export interface BaseUserChannel {
  id: string
  name: string
  banner: string
  category: string
  createdOn: string
  channelplaylistSet: Arrayable<ChannelPlaylistSet>
  description: string
  email?: string
  facebook?: string
  instagram?: string
  tiktok?: string
  isVerified: boolean
  reference: string
  tags: Tag[]
  subscribers: Arrayable<Subscriber>
}
