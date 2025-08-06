import { defineStore } from 'pinia'
import type { VideoItem } from '~/types'

export const useFeedStore = defineStore('feed', () => {    
    const items = ref<VideoItem[]>([])
    const isLoading = ref(false)

    // const { ws } = useWebSocket()

    return {
        items,
        isLoading
    }
})
