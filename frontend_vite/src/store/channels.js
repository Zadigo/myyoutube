import { defineStore } from 'pinia'

const useChannels = defineStore('channels', {
  state: () => ({
    currentChannel: {}
  })
})

export {
  useChannels
}
