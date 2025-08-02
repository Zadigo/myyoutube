import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { VideoInfo, VideosFeedResponseData } from '~/types'

export const useFeed = defineStore('feed', () => {
  const videos = ref<VideosFeedResponseData[]>([])
  const currentVideo = ref<VideoInfo>()

  const hasVideos = computed(() => videos.value.length > 0)

  return {
    videos,
    /**
     * @deprecated
     */
    currentVideo,
    hasVideos
  }
})
