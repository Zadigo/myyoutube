import { defineStore } from 'pinia'
import type { VideoItem } from '~/types'

export const useVideoStore = defineStore('videos', () => {    
    const items = ref<VideoItem[]>([])
    const isLoading = ref(false)

    // const { ws } = useWebSocket()

    return {
        items,
        isLoading
    }
})
