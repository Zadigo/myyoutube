import { userChannelsFixture } from '~/utils/fixtures/channels'

export default defineEventHandler(async (_event) => {
  return userChannelsFixture
})
