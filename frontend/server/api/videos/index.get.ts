import type { VideoInfo } from '~/apps/types'
import { refreshAccessToken } from '~/apps/utils'

export default defineEventHandler(async event => {
  const refreshToken = getCookie(event, 'refresh')
  const id = getRouterParam(event, 'id') as string

  const response = await $fetch<VideoInfo>(`/api/v1/videos/${id}`, {
    baseURL: useRuntimeConfig().public.djangoProdUrl,
    onRequestError({ error, response }) {
      if (response?.status === 401) {
        refreshAccessToken(refreshToken)
      }
    }
  })

  return response
})
