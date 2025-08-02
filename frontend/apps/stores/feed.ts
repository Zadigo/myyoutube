import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { VideoInfo } from '~/apps/types'

export const useFeed = defineStore('feed', () => {
  const videos = ref<VideoInfo[]>([])
  const currentVideo = ref<VideoInfo>()

  const hasVideos = computed(() => {
    return videos.value.length > 0
  })

  return {
    videos,
    currentVideo,
    hasVideos
  }
})
