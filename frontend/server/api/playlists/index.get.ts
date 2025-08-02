import { refreshAccessToken } from '~/app/utils'

import type { Playlist } from '~/app/types'

export default defineEventHandler(async (event) => {
  const refresh = getCookie(event, 'refresh')

  return await $fetch<Playlist[]>('/api/v1/playlists', {
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
