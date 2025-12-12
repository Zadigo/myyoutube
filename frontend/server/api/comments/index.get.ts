import { commentsFixture } from '~/data/fixtures/comments'

export default defineEventHandler(async (_event) => {
  return commentsFixture
})
