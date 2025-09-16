import { defineStore } from 'pinia'

import type { DefaultMainCategories, DefaultSortBy, DefaultUploadDate, DefaultVideoLength } from '~/data'
import type { VideoInfo, VideosFeedResponseData } from '~/types'

/**
 * Store to manage videos on the feed
 * @see ~/composables/use/feed.ts
 * @deprecated Use the composable instead
 */
export const useFeedStore = defineStore('feed', () => {
  const videos = ref<VideosFeedResponseData[]>([])

  const hasVideos = computed(() => videos.value.length > 0)

  /**
   * Search
   */

  const search = ref<string>('')
  const category = ref<DefaultMainCategories>('All')
  const videoLength = ref<DefaultVideoLength>('4-20 minutes')
  const uploadDate = ref<DefaultUploadDate>('This week')
  const sortBy = ref<DefaultSortBy>('Upload date')

  return {
    search,
    category,
    videoLength,
    uploadDate,
    sortBy,
    /**
     * List of videos in the feed
     */
    videos,
    /**
     * Indicates if the feed has any videos
     */
    hasVideos
  }
})

/**
 * Store for managing video details
 */
export const useVideoDetailStore = defineStore('videoDetail', () => {
  const currentVideo = ref<VideoInfo>()
  const isLoading = ref<boolean>(true)

  function getVideo() {
    if (!currentVideo.value) {
      try {
        const { id: videoId } = useRoute().params as { id: string }
        const { data } = useFetch<VideoInfo>(`/api/videos/${videoId}`, {
          method: 'GET',
          immediate: true
        })

        console.log('useVideoDetailStore', data, isLoading)

        if (data.value) {
          isLoading.value = false
          currentVideo.value = data.value
        }
      } catch (e) {
        console.log(e)
      }
    }
  }

  return {
    getVideo,
    isLoading,
    currentVideo
  }
})
