import type { DefaultMainCategories, DefaultSortBy, DefaultUploadDate, DefaultVideoLength } from '~/data'
import type { Feed, SearchQuery } from '~/types'

/**
 * 
 */
export async function useSearchFeedComposable() {
  const search = ref<string>('')

  const searched = refDebounced(search, 500)
  const { history } = useRefHistory(searched)

  watchArray(history, () => {
    // Update firebase
  })

  const category = ref<DefaultMainCategories>('All')
  const videoLength = ref<DefaultVideoLength>('4-20 minutes')
  const uploadDate = ref<DefaultUploadDate>('This week')
  const sortBy = ref<DefaultSortBy>('Upload date')

  /**
   * Update URL parameters when the search query or filters change
   */
  
  const query = useUrlSearchParams() as SearchQuery

  watch([search, category, videoLength, uploadDate, sortBy], (newValues) => {
    const [newSearch, newCategory, newVideoLength, newUploadDate, newSortBy] = newValues

    query.search = newSearch || undefined
    query.category = newCategory !== 'All' ? newCategory : undefined
    query.videoLength = newVideoLength !== '4-20 minutes' ? newVideoLength : undefined
    query.uploadDate = newUploadDate !== 'This week' ? newUploadDate : undefined
    query.sortBy = newSortBy !== 'Upload date' ? newSortBy : undefined
  })

  const { data, execute } = await useFetch<Feed>('/api/videos', {
    method: 'GET',
    immediate: false,
    watch: [search, category, videoLength, uploadDate, sortBy],
    key: `videos-feed-${search.value}-${category.value}-${videoLength.value}-${uploadDate.value}-${sortBy.value}`
  })

  return {
    search,
    category,
    videoLength,
    uploadDate,
    sortBy,
    data,
    execute
  }
}

/**
 * Composable for fetching and managing a video feed
 */
export const useFeedComposable = createSharedComposable(() => {
  const videos = computedAsync<Feed>(async () => {
    return await $fetch<Feed>('/api/videos', {
      method: 'GET'
    })
  }, [], {
    onError(e) {
      console.error('Error fetching feed videos:', e)
    },
  })

  const hasVideos = computed(() => isDefined(videos) ? videos.value?.allVideos?.edges.length > 0 : false)

  return {
    /**
     * List of videos in the feed
     * @default []
     */
    videos,
    /**
     * Indicates if the feed has any videos
     * @default false
     */
    hasVideos
  }
})
