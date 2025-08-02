import { refreshAccessToken } from '~/app/utils'

import type { VideosFeedResponseData } from '~/app/types'

export default defineCachedEventHandler(async (event) => {
  const refresh = getCookie(event, 'refresh')

  return await $fetch<VideosFeedResponseData>('/api/v1/notifications/profile', {
    baseURL: useRuntimeConfig().public.djangoProdUrl,
    onRequestError({ response, error }) {
      if (response) {
        if (response.status === 401) {
          refreshAccessToken(refresh)
          console.log(error)
        }
      }
    }
  })
})
