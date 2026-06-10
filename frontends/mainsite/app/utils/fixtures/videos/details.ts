import type { VideoDetails } from "~/types"
import { getRandomVideoPath } from "../utils"

export const videoDetailsFixture: VideoDetails = {
  id: "1",
  title: "Sample Video Title",
  description: "This is a sample video description.",
  video: getRandomVideoPath(),
  videoId: "vid_sample123",
  views: 543215,
  active: true,
  ageRestricted: false,
  category: "Entertainment",
  commentStrategy: "default",
  duration: 300,
  framerate: 30,
  height: 720,
  width: 1280,
  modifiedOn: "2024-06-15T12:00:00Z",
  ratingsAreVisible: true,
  recordingDate: "2024-06-10T14:00:00Z",
  recordingLanguage: "en",
  visibility: "public",
  recordingLocation: "New York, USA",
  createdOn: "2024-06-15T10:00:00Z",
  userChannel: {
    id: "VXNlckNoYW5uZWxOb2RlOjI=",
    name: "Sample Channel",
    banner: "/banners/sample-banner.png",
    category: "Entertainment",
    createdOn: "2023-01-01T09:00:00Z",
    channelplaylistSet: [],
    description: "This is a sample channel description.",
    isVerified: true,
    reference: "eAsySampleChannel",
    tags: [],
    subscribers: []
  },
  user: {
    id: 2,
    username: "sampleuser",
    firstname: "Sample",
    lastname: "User",
    get_full_name: "Sample User",
    userProfile: {
      avatar: "/avatars/avatar1.png",
      birthdate: "1990-05-20",
      isProfessional: false,
      zipCode: null,
      city: null,
      address: null,
      telephone: null,
      createdOn: "2022-12-12T08:00:00Z",
      customerId: null,
      id: "U2FtcGxlVXNlck5vZGU6Mg=="
    }
  } 
}
