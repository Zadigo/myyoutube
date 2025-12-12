import { userChannelsFixture } from '~/data/fixtures/channels'

export default defineEventHandler(async (_event) => {
  return userChannelsFixture
})
