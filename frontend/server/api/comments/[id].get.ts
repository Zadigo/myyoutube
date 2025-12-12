import { repliesFixture } from '~/data/fixtures/comments'

export default defineEventHandler(async (_event) => {
  return repliesFixture
})
  