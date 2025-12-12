// import { refreshAccessToken } from '~/utils'
import { videoDetailsFixture } from '~/data/fixtures/videos'

export default defineEventHandler(async event => {
  // const refreshToken = getCookie(event, 'refresh')
  
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
        
  const id = getRouterParam(event, 'id') as string
  
  console.log('Fetching video details for ID:', id)

  // const response = await $fetch<GraphQlResponse<'searchvideos', VideoDetails>>('/graphql/', {
  //   method: 'POST',
  //   baseURL: useRuntimeConfig().public.videosGraphqlUrl,
  //   body: {
  //     query: `
  //       query {
  //         searchvideos(videoId: "${id}") {
  //           edges {
  //             node {
  //               id
  //               title
  //               description
  //               video
  //             }
  //           }
  //         }
  //       }
  //     `
  //   }
  // })

  // console.log('Video details response:', response.data.searchvideos.edges[0].node)

  return videoDetailsFixture
})
