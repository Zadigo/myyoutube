import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { VideoInfo, VideosFeedResponseData } from '~/types'

export const useFeedStore = defineStore('feed', () => {
  const videos = reactive<VideosFeedResponseData[]>([])

  const currentVideo = ref<VideoInfo>()

  const hasVideos = computed(() => videos.length > 0)

  return {
    videos,
    /**
     * @deprecated
     */
    currentVideo,
    /**
     * Indicates if the feed has any videos
     */
    hasVideos
  }
})
