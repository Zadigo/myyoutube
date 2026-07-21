import { feedVideoFixtures } from '~/utils/fixtures/videos'
import type { SearchQuery, Feed } from '~/types'
import { generateErrorTemplate } from '~/utils/errors'

export default defineEventHandler(async event => {
  try {
    const query = getQuery<SearchQuery>(event)

    const response = await $fetch<Feed>('/graphql/', {
      method: 'POST',
      baseURL: useRuntimeConfig().public.videosGraphqlUrl,
      body: {
        query: `
          query {
            allVideos(first: 100) {
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
              }
              pageInfo {
                startCursor
                endCursor
                hasNextPage
                hasPreviousPage
              }
            }
          }
        `,
        variables: {
          name: query.name || null,
          category: query.category || null,
          uploadDate: query.uploadDate || null,
          sortBy: query.sortBy || null,
        }
      }
    })

    console.log('Feed Videos Response:', JSON.stringify(response))

    return feedVideoFixtures
  } catch (error) {
    console.error('Error fetching feed videos:', error)
    const template = generateErrorTemplate(error)
    return createError(template)
  }
})
