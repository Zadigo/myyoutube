import { defineStore } from 'pinia'
import { Video } from '../types/feed'

interface RootState {
    videos: Video[],
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

