import { createErrorTemplate } from '~/utils'
// import jsonFeed from '~~/public/fixtures/feed.json'

import { faker } from '@faker-js/faker'

export default defineEventHandler(async event => {
  try {
    const _id = getRouterParam(event, 'id') as string
    // const video = jsonFeed.data.allVideos.edges.find(edge => edge.node.videoId === id)

    // const { singleItem } = useLoadFixtures()
    // const video = singleItem()
    // return {
    //   ...video,
    //   userChannel: {
    //     reference: `ch_${faker.string.uuid()}`,
    //     name: faker.person.firstName(),
    //   }
    // } as VideoDetails

    return {
      id: "VmlkZW9zVAlrZTox",
      title: "My First Video",
      description: faker.lorem.paragraph({ min: 2, max: 7 }),
      modifiedOn: faker.date.recent().toISOString(),
      ratingsAreVisible: true,
      recordingDate: "2026-03-23T19:22:51+00:00",
      recordingLanguage: "FRENCH",
      recordingLocation: null,
      video: `/videos/vid${faker.number.int({ min: 1, max: 9 })}.mp4`,
      videoId: "vid_i97D2nzmKCSNLzX",
      views: faker.number.int({ min: 0, max: 150000 }),
      width: 0,
      height: 0,
      visibility: "PUBLIC",
      createdOn: faker.date.past().toISOString(),
      userChannel: {
        reference: `ch_${faker.string.uuid()}`,
        name: faker.person.firstName(),
        user: {
          userProfile: {
            avatar: "/avatars/default.png"
          }
        }
      }
    } as VideoDetails
  } catch (error) {
    const template = createErrorTemplate(error)
    throw createError(template)
  }
})
