import { UserChannel } from '../types/channels'
import { defineStore } from 'pinia'

interface RootState {
  currentChannel: UserChannel | null
}

const useChannels = defineStore('channels', {
  state: (): RootState => ({
    currentChannel: null
  })
})

export {
  useChannels
}
