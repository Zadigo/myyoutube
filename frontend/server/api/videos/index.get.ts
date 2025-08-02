import type { VideosFeedResponseData } from '~/types'
import { fixtureVideos } from '~/data/fixtures'

export default defineEventHandler(async event => {
  // const query = getQuery<{ q: string }>(event)

  // const response = await $fetch<VideosFeedResponseData>('/v1/videos', {
  //   baseURL: useRuntimeConfig().public.djangoProdUrl,
  //   params: {
  //     q: query.q
  //   }
  // })

  // return response
  return fixtureVideos
})
