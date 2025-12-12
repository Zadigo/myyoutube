import type { Arrayable, BaseUserChannel } from '.'
import type { BaseUser } from './accounts'
import type { GraphQlData, RelayEdge, RelayNode } from './graphql'


export type BaseComment = {
  id: string
  content: string
  fromCreator: boolean
  pinned: boolean
  numberOfReplies: number
  createdOn: string
} & { 
  user: Pick<BaseUser, 'id' | 'username'> & { userChannelSet: Arrayable<Pick<BaseUserChannel, 'id' | 'name' | 'reference'>>}
}

// export interface Reply extends BaseComment {}

export type VideoCommentNode = RelayNode<BaseComment>

export type VideoComments = GraphQlData<'videocomments', RelayEdge<BaseComment>>

export type VideoReply = BaseComment

export type VideoReplyNode = RelayNode<Reply>
