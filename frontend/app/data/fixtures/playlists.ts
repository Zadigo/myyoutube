import type { Playlist } from '~/types'

export const playlistsFixture: Playlist[] = [
  {
    id: 4,
    name: "Kendall Jenner",
    description: "My kendall Jenner playlist",
    videos: [],
    visibility: "Public",
    created_on: "2025-03-25T23:34:17.619177Z"
  },
  {
    id: 5,
    name: "Photoshop",
    description: "My photoshop playlist",
    videos: [],
    visibility: "Public",
    created_on: "2025-03-25T23:36:35.412430Z"
  },
  {
    id: 6,
    name: "Kendall Jenner",
    description: "A playlist that contains videos of Kendall Jenner",
    videos: [
      {
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
          firstname: 'my firstname',
          lastname: 'my lastname',
          username: "qtigawWIuWyJv5T",
          get_full_name: "None None"
        },
        created_on: "2025-03-26T17:17:59.525486Z"
      }
    ],
    visibility: "Private",
    created_on: "2025-03-25T23:36:58.677237Z"
  }
]
