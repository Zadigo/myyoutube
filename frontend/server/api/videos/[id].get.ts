// import type { VideoInfo } from '~/types'
// import { refreshAccessToken } from '~/utils'
import { fixtureVideo } from '~/data/fixtures/videos'

export default defineEventHandler(async event => {
  // const refreshToken = getCookie(event, 'refresh')
  // const id = getRouterParam(event, 'id') as string

  // const response = await $fetch<VideoInfo>(`/v1/videos/${id}`, {
  //   method: 'GET',
  //   baseURL: useRuntimeConfig().public.djangoProdUrl,
  //   headers: { 'Content-Type': 'application/json' },
  //   onRequestError({ _error, response }) {
  //     if (response?.status === 401) {
  //       refreshAccessToken(refreshToken)
  //     }
  //   }
  // })

  // return response

  return fixtureVideo
})
