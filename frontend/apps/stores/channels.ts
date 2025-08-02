import type { UserChannel } from '~/apps/types'
import { defineStore } from 'pinia'

export const useChannels = defineStore('channels', () => {
  const currentChannel = ref<UserChannel>()

  return {
    currentChannel
  }
})
