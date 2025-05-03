import { refreshAccessToken } from '~/utils'

import type { NotificationProfile } from '~/types'

export default defineCachedEventHandler(async (event) => {
  const refresh = getCookie(event, 'refresh')

  return await $fetch<NotificationProfile>('/api/v1/notifications/profile', {
    baseURL: useRuntimeConfig().public.djangoProdUrl,
    params: {},
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
