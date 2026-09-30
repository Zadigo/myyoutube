import { faker } from '@faker-js/faker'
import type { Arrayable } from '#shared/types/utils'
import type { VideoCommentNode, VideoComments, VideoReplies } from '#shared/types/comments'

const commentNodes = (n: number) => {
  return Array.from<Arrayable<VideoCommentNode>>({ length: n }).map((_, index) => ({
    node: {
      id: `comment${index + 1}`,
      content: faker.lorem.paragraph({ min: 1, max: 10 }),
      fromCreator: faker.datatype.boolean({ probability: 0.2 }),
      pinned: index === 0,
      numberOfReplies: 2,
      createdOn: faker.date.past().toISOString(),
      user: {
        id: index + 1,
        username: faker.person.fullName(),
        userChannelSet: [
          {
            id: `ch_${faker.string.uuid()}`,
            name: `Channel ${index + 1}`,
            reference: `ch_${faker.string.uuid()}`
          }
        ]
      }
    }
  }))
}

export const commentsFixture: VideoComments = {
  data: {
    videocomments: {
      edges: commentNodes(15)
    }
  }
}

export const repliesFixture: VideoReplies = {
  data: {
    commentreplies: {
      edges: commentNodes(5)
    }
  }
}
