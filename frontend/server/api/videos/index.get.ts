// import type { VideosFeedResponseData } from '~/types'
import { fixtureVideos } from '~/data/fixtures'
import type { SearchQuery } from '~/types'

export default defineEventHandler(async event => {
  const query = getQuery<SearchQuery>(event)

  // const response = await $fetch<VideosFeedResponseData>('/v1/videos', {
  //   baseURL: useRuntimeConfig().public.djangoProdUrl,
  //   params: {
  //     q: query.search
  //   }
  // })

  console.log(query)

  return fixtureVideos
})
