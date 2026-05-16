import type { FeedVideoNode } from '~/types'
import { videoPaths } from '../utils'
import { faker } from '@faker-js/faker'

export const feedVideoFixture: FeedVideoNode = {
  node: {
    id: faker.string.uuid(),
    title: 'Girl dancing happily',
    description: 'Some awesome description',
    video: '/videos/vid3.mp4',
    videoId: 'vid_HzLYGFSu1mOjSGn',
    views: 12345,
    createdOn: '2024-06-10T12:00:00Z',
    category: 'Entertainment',
    ageRestricted: false,
    userChannel: {
      id: faker.string.uuid(),
      name: "John's Channel",
      reference: 'johns-channel',
      user: {
        id: faker.number.int(),
        username: 'john_doe',
        userProfile: {
          avatar: 'https://i.pravatar.cc/150?img=3'
        }
      }
    }
  } 
}

export const feedVideoFixtures: FeedVideoNode[] = videoPaths.map((path) => {
  const newFixture = { ...feedVideoFixture }

  newFixture.node.id = faker.string.uuid()
  newFixture.node.video = path
  newFixture.node.videoId = `vid_${faker.string.alphanumeric(16)}`
  newFixture.node.title = faker.lorem.sentence({ min: 1, max: 3 })
  newFixture.node.description = faker.lorem.paragraph()
  newFixture.node.views = faker.number.int({ min: 0, max: 1000000 })
  newFixture.node.createdOn = faker.date.past().toISOString()
  newFixture.node.category = faker.helpers.arrayElement(['Entertainment', 'Education', 'Music', 'Gaming', 'Vlogs'])
  newFixture.node.ageRestricted = faker.datatype.boolean()
  newFixture.node.userChannel.id = faker.string.uuid()
  newFixture.node.userChannel.name = faker.person.fullName()
  newFixture.node.userChannel.reference = faker.helpers.slugify(newFixture.node.userChannel.name).toLowerCase()
  newFixture.node.userChannel.user.id = faker.number.int()
  newFixture.node.userChannel.user.username = faker.person.firstName().toLowerCase() + '_' + 'doe'

  return newFixture
})

export function selectRandomVideo(): FeedVideoNode {
  const randomIndex = Math.floor(Math.random() * feedVideoFixtures.length)
  return feedVideoFixtures[randomIndex]
}
