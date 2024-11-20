import { defineStore } from 'pinia'

export default defineStore('feed', {
    state: () => ({
        items: [],
        isLoading: false
    })
})
