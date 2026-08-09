import { faker } from '@faker-js/faker'
import type { VideoDetails } from '~/types'

export const videoDetailsFixture: VideoDetails = {
  id: faker.number.int({ min: 1, max: 1000 }).toString(),
  videoId: faker.string.uuid(),
  title: faker.lorem.sentence(),
  description: faker.lorem.paragraphs(2),
  video: faker.internet.url(),
  active: true,
  createdOn: faker.date.past().toISOString(),
  ageRestricted: faker.datatype.boolean(),
  category: faker.lorem.word(),
  commentStrategy: faker.lorem.word(),
  duration: faker.number.int({ min: 30, max: 3600 }),
  framerate: faker.number.int({ min: 24, max: 60 }),
  height: faker.number.int({ min: 240, max: 1080 }),
  modifiedOn: faker.date.past().toISOString(),
  ratingsAreVisible: faker.datatype.boolean(),
  recordingDate: faker.date.past().toISOString(),
  recordingLanguage: faker.lorem.word(),
  recordingLocation: faker.location.city(),
  visibility: faker.lorem.word(),
  views: faker.number.int({ min: 0, max: 1000000 }),
  width: faker.number.int({ min: 320, max: 1920 }),
  userChannel: {
    id: faker.string.uuid(),
    reference: faker.lorem.word(),
    name: faker.company.name(),
    banner: faker.image.url(),
    category: faker.lorem.word(),
    channelplaylistSet: [],
    createdOn: faker.date.past().toISOString(),
    description: faker.lorem.paragraphs(2),
    isVerified: faker.datatype.boolean(),
    subscribers: [
      {
        node: {
          id: faker.number.int({ min: 1, max: 1000 }),
          username: faker.person.firstName()
        }
      }
    ],
    tags: [
      {
        id: faker.string.uuid(),
        name: faker.lorem.word()
      }
    ],
    email: faker.internet.email(),
    facebook: faker.internet.url()  ,
    instagram: faker.internet.url(),
    tiktok: faker.internet.url(),
    user: {
      id: faker.number.int({ min: 1, max: 1000 }),
      username: faker.person.firstName(),
      userProfile: {
        avatar: faker.image.avatar()
      }
    }
  },
  user: {
    id: faker.number.int({ min: 1, max: 1000 }),
    username: faker.person.firstName(),
    firstname: faker.person.firstName(),
    lastname: faker.person.lastName(),
    get_full_name: faker.person.fullName(),
    userProfile: {
      id: faker.string.uuid(),
      createdOn: faker.date.past().toISOString(),
      avatar: faker.image.avatar(),
      birthdate: faker.date.past().toISOString(),
      isProfessional: faker.datatype.boolean(),
      address: faker.location.streetAddress(),
      city: faker.location.city(),
      customerId: faker.string.uuid(),
      telephone: faker.phone.number(),
      zipCode: faker.location.zipCode()
    }
  }
}
