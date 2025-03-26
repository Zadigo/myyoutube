import { defineStore } from 'pinia'

export const useFeed = defineStore('feed', () => {
    const items = ref([])
    const isLoading = ref(false)

    return {
        items,
        isLoading
    }
})
