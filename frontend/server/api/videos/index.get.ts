import { fixtureVideos } from '~/data/fixtures'
import type { SearchQuery, BaseVideo, GraphQlResponse } from '~/types'

export default defineEventHandler(async event => {
  const query = getQuery<SearchQuery>(event)

  const response = await $fetch<GraphQlResponse<'allvideos', BaseVideo>>('/graphql/', {
    method: 'POST',
    baseURL: useRuntimeConfig().public.videosGraphqlUrl,
    body: {
      query: `
        query {
          allvideos {
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

  return fixtureVideos
})
