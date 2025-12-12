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
          allvideos(first: 100) {
            edges {
              node {
                id
                ageRestricted
                category
                createdOn
                commentStrategy
                description
                duration
                framerate
                height
                modifiedOn
                ratingsAreVisible
                recordingDate
                recordingLanguage
                recordingLocation
                title
                userChannel {
                  isVerified
                  name
                  reference
                }
                video
                videoId
                views
                visibility
                width
                user {
                  userprofile {
                    isProfessional
                  }
                }
              }
              pageInfo {
                startCursor
                endCursor
                hasNextPage
                hasPreviousPage
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
