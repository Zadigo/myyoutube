import type { VideoComment } from '~/types'

export const commentsFixture: VideoComment[] = [
  {
    id: 2,
    user: {
      id: 1,
      firstname: null,
      lastname: null,
      username: "qtigawWIuWyJv5T",
      get_full_name: "None None"
    },
    content: "What do you expect from use",
    from_creator: true,
    pinned: true,
    number_of_replies: 0,
    is_liked: false,
    is_disliked: false,
    created_on: "2025-08-03T11:58:57.669585Z",
    user_channel: "ch_N6GUfe7iX7QvOwL"
  },
  {
    id: 1,
    user: {
      id: 1,
      firstname: null,
      lastname: null,
      username: "qtigawWIuWyJv5T",
      get_full_name: "None None"
    },
    content: "This is some content to use",
    from_creator: true,
    pinned: false,
    number_of_replies: 0,
    is_liked: false,
    is_disliked: false,
    created_on: "2025-08-03T11:58:33.964772Z",
    user_channel: "ch_N6GUfe7iX7QvOwL"
  }
]
