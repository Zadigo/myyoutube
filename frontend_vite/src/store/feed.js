import { defineStore } from 'pinia'

const useFeed = defineStore('feed', {
  state: () => ({
    videos: []
  })
})

export {
  useFeed
}
