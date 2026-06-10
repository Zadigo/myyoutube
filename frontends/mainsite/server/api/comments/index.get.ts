import { commentsFixture } from '~/utils/fixtures/comments'

export default defineEventHandler(async (_event) => {
  return commentsFixture
})
