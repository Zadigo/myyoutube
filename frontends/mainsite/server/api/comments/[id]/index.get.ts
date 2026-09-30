import { repliesFixture } from '#server/utils/testing/comments'

/**
 * Return all the replies for a specific comment
 */
export default defineEventHandler(async (_event) => {
  return repliesFixture
})
  