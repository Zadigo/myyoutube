import type { VideosFeedResponseData } from '~/app/types'

export default defineEventHandler(async event => {
  const query = getQuery<{ q: string }>(event)

  const response = await $fetch<VideosFeedResponseData>('/api/v1/videos', {
    baseURL: useRuntimeConfig().public.djangoProdUrl,
    params: {
      q: query.q
    }
  })

  return response
})
