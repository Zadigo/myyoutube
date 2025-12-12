// import { refreshAccessToken } from '~/utils'
import { fixtureVideos } from '~/data/fixtures/videos'
import type { BaseVideo, GraphQlResponse } from '~/types'

export default defineEventHandler(async event => {
  // const refreshToken = getCookie(event, 'refresh')
  const id = getRouterParam(event, 'id') as string

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

  const response = await $fetch<GraphQlResponse<'allvideos', BaseVideo>>('/graphql/', {
    method: 'POST',
    baseURL: useRuntimeConfig().public.videosGraphqlUrl,
    body: {
      query: `
        query {
          allvideos(first: 100) {
            edges {
              node {
                id
                title
                description
                user {
                  id
                  username
                }
              }
            }
          }
        }
      `
    }
  })

  console.log('Response:', JSON.stringify(response))
  console.log(query)

  return fixtureVideos.find(video => video.video_id === id)
})
