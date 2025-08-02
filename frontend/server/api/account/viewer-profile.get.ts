import type { ViewingProfile } from '~/types'
import { refreshAccessToken } from '~/utils'

export default defineCachedEventHandler(async event => {
  const refresh = getCookie(event, 'refresh')

  const response = await $fetch<ViewingProfile>('/api/v1/accounts/viewing-profile', {
    method: 'GET',
    baseURL: useRuntimeConfig().public.djangoProdUrl,
    onRequestError({ response }) {
      if (response?.status === 401) {
        refreshAccessToken(refresh)
      }
    }
  })
  return response
}, {
  base: 'redis',
  maxAge: 30 * 60
})
