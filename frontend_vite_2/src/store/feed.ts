import { defineStore } from 'pinia'
import { VideosFeedResponseData, Video } from '../types/feed'

interface RootState {
    videos: VideosFeedResponseData[],
    currentVideo: Video | null
}

const useFeed = defineStore('feed', {
  state: (): RootState => ({
    videos: [],
    currentVideo: null
  })
})

export {
  useFeed
}

