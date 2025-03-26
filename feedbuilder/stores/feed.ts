import { defineStore } from 'pinia'
import type { VideoItem } from '~/types'

export const useFeed = defineStore('feed', () => {
    // const items = ref(Array.from({ length: 10 }).map((a, b) => {
    //   return {
    //     id: b
    //   }
    // }))
    
    const items = ref<VideoItem[]>([])
    const isLoading = ref(false)

    return {
        items,
        isLoading
    }
})
