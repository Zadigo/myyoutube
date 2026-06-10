import type { Playlist } from '~/types'

export default defineEventHandler(async (event) => {
  const refresh = getCookie(event, 'refresh')

  return await $fetch<Playlist[]>('/v1/playlists', {
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
