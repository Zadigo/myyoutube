import { createErrorTemplate } from '~/utils'

export default defineEventHandler(async event => {
  const _id = getRouterParam(event, 'id') as string

  try {
    const { singleItem } = useLoadFixtures()
    const video = singleItem()
    return {
      ...video,
      userChannel: {
        reference: '12323',
        name: 'Sample Channel',
        
      }
    } as VideoDetails
    // $fetch('/graphql/', {
    //   method: 'POST',
    //   headers: [
    //     ['Content-Type', 'application/json'],
    //     ['Accept', 'application/json'],
    //   ],
    // })
    // return feedVideoFixtures.find(video => video.videoId === id) || null
  } catch (error) {
    const template = createErrorTemplate(error)
    throw createError(template)
  }


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
})
