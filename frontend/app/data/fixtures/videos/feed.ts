import type { FeedVideo } from '~/types'
import { videoPaths } from '../utils'

export const feedVideoFixture: FeedVideo = {
  id: 'VmlkZW9zTm9kZTox',
  title: 'Girl dancing happily',
  description: 'Some awesome description',
  video: '/videos/vid3.mp4',
  videoId: 'vid_HzLYGFSu1mOjSGn',
  views: 12345,
  createdOn: '2024-06-10T12:00:00Z',
  userChannel: {
    id: 'VXNlckNoYW5uZWxOb2RlOjE=',
    name: 'John\'s Channel',
    reference: 'johns-channel'
  },
  user: {
    id: 1,
    username: 'johndoe',
    userProfile: {
      avatar: '/avatars/avatar1.png'
    }
  } 
}

export const feedVideoFixtures: FeedVideo[] = videoPaths.map((path, index) => {
  const newFixture = { ...feedVideoFixture }

  newFixture.id = `VmlkZW9zTm9kZTox${index}`
  newFixture.video = path
  newFixture.videoId = `vid_HzLYGFSu1mOjSGn${index}`
  newFixture.title = `Sample Video Title ${index + 1}`
  newFixture.views = Math.floor(Math.random() * 100000)

  return newFixture
})
