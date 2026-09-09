import { createErrorTemplate } from '~/utils/errors'
import jsonFeed from '~~/public/fixtures/feed.json'

export default defineEventHandler(async (_event) => {
  try {
    console.log(jsonFeed)
    return jsonFeed as FeedVideos

    // const _query = getQuery<SearchQuery>(event)
    // const { toPaginated, fixtures } = useLoadFixtures()
    // return toPaginated(fixtures)

    // await $fetch<Feed>('/graphql/', {
    //   method: 'POST',
    //   baseURL: useRuntimeConfig().public.videosGraphqlUrl,
    //   body: {
    //     query: `
    //       query {
    //         allVideos(first: 100) {
    //           edges {
    //             node {
    //               id
    //               ageRestricted
    //               category
    //               createdOn
    //               commentStrategy
    //               description
    //               duration
    //               framerate
    //               height
    //               modifiedOn
    //               ratingsAreVisible
    //               recordingDate
    //               recordingLanguage
    //               recordingLocation
    //               title
    //               userChannel {
    //                 isVerified
    //                 name
    //                 reference
    //               }
    //               video
    //               videoId
    //               views
    //               visibility
    //               width
    //               user {
    //                 userprofile {
    //                   isProfessional
    //                 }
    //               }
    //             }
    //           }
    //           pageInfo {
    //             startCursor
    //             endCursor
    //             hasNextPage
    //             hasPreviousPage
    //           }
    //         }
    //       }
    //     `
    //   }
    // })
  } catch (error) {
    console.error('Error fetching feed videos:', error)
    const template = createErrorTemplate(error)
    return createError(template)
  }
})
