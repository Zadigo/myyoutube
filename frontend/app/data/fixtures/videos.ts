import type { VideoInfo, VideosFeedResponseData } from '~/types'

export const fixtureVideos: VideosFeedResponseData[] = [
  {
    id: 2,
    title: 'Girl dancing happily',
    description: 'Some awesome description',
    video_id: 'vid_HzLYGFSu1mOjSGn',
    user_channel: {
      id: 1,
      reference: 'ch_N6GUfe7iX7QvOwL',
      name: 'Hello Kittty',
      number_of_subscribers: 0,
      number_of_playlists: 0,
      channelplaylist_set: [],
      tags: [
        {
          id: 1,
          name: 'Music'
        },
        {
          id: 2,
          name: 'Dancing'
        }
      ]
    },
    age_restricted: true,
    video: 'http://127.0.0.1:8000/media/uploads/ch_N6GUfe7iX7QvOwL/8a1963a4c665245f595e0ed324ca6f.mp4',
    channel_playlist: null,
    user: {
      id: 1,
      firstname: null,
      lastname: null,
      username: 'qtigawWIuWyJv5T',
      get_full_name: 'None None'
    },
    created_on: '2025-03-26T17:17:59.525486Z'
  },
  {
    id: 1,
    title: 'Girl dancing till she is happy',
    description: 'This is a simple description that can be used for us',
    video_id: 'vid_PMP128hTb5i3grC',
    user_channel: {
      id: 1,
      reference: 'ch_N6GUfe7iX7QvOwL',
      name: 'Hello Kittty',
      number_of_subscribers: 0,
      number_of_playlists: 0,
      channelplaylist_set: [],
      tags: [
        {
          id: 1,
          name: 'Music'
        },
        {
          id: 2,
          name: 'Dancing'
        }
      ]
    },
    age_restricted: false,
    video: 'http://127.0.0.1:8000/media/uploads/ch_N6GUfe7iX7QvOwL/c0fdf6706a3acb1ad04f1b64b62af6.mp4',
    channel_playlist: null,
    user: {
      id: 1,
      firstname: null,
      lastname: null,
      username: 'qtigawWIuWyJv5T',
      get_full_name: 'None None'
    },
    created_on: '2025-03-23T17:35:35.938100Z'
  }
]

export const fixtureVideo: VideoInfo = {
  id: 2,
  title: "Girl dancing happily",
  description: "Some awesome description",
  video_id: "vid_HzLYGFSu1mOjSGn",
  user_channel: {
    id: 1,
    reference: "ch_N6GUfe7iX7QvOwL",
    name: "Hello Kittty",
    number_of_subscribers: 0,
    number_of_playlists: 0,
    channelplaylist_set: [],
    tags: [
      {
        id: 1,
        name: "Music"
      },
      {
        id: 2,
        name: "Dancing"
      }
    ]
  },
  age_restricted: true,
  video: "http://127.0.0.1:8000/media/uploads/ch_N6GUfe7iX7QvOwL/8a1963a4c665245f595e0ed324ca6f.mp4",
  channel_playlist: null,
  user: {
    id: 1,
    firstname: null,
    lastname: null,
    username: "qtigawWIuWyJv5T",
    get_full_name: "None None"
  },
  created_on: "2025-03-26T17:17:59.525486Z"
}
