import { commentsFixture } from '#server/utils/testing/comments'

export default defineEventHandler(async (_event) => {
  return commentsFixture
})
