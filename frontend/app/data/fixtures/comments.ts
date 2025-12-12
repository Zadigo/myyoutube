import type { Arrayable, VideoCommentNode, VideoComments } from '~/types'

const commentNodes = Array.from<Arrayable<VideoCommentNode>>({ length: 50 }).map((_, index) => ({
  node: {
    id: `comment${index + 1}`,
    content: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Comment number ${index + 1}.`,
    fromCreator: index % 2 === 0,
    pinned: index === 0,
    numberOfReplies: 2,
    createdOn: new Date(2024, 5, index + 1, 12, 0, 0).toISOString(),
    user: {
      id: index + 1,
      username: `User${index + 1}`,
      userChannelSet: [
        {
          id: `channel${index + 1}`,
          name: `Channel ${index + 1}`,
          reference: `channel-reference-${index + 1}`
        }
      ]
    }
  }
}))

export const commentsFixture: VideoComments = {
  data: {
    videocomments: {
      edges: commentNodes
    }
  }
}
