import type { Feed, SearchQuery } from '#shared/types/feed'

/**
 * Composable for managing the search feed, including search query, filters, and URL synchronization.
 */
export const useSearchFeedComposable = createSharedComposable(async () => {
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

  // const { data, execute } = await useFetch<Feed>('/api/videos', {
  //   method: 'GET',
  //   immediate: false,
  //   watch: [search, category, videoLength, uploadDate, sortBy],
  //   key: `videos-feed-${search.value}-${category.value}-${videoLength.value}-${uploadDate.value}-${sortBy.value}`
  // })

  const { data, execute } = await useAsyncData(`feed-${search.value}-${category.value}-${videoLength.value}-${uploadDate.value}-${sortBy.value}`, async () => $fetch<Feed>('/api/videos', {
    method: 'GET'
  }), {
    default: () => ({} as Feed)
  })

  const hasVideos = computed(() => toValue(data).data.allVideos.edges.length > 0)

  return {
    hasVideos,
    search,
    category,
    videoLength,
    uploadDate,
    sortBy,
    data,
    execute
  }
})

/**
 * Composable for fetching and managing a video feed
 */
export const useFeedComposable = createSharedComposable(() => {
  const videos = computedAsync<Feed>(
    async () => await $fetch<Feed>('/api/videos', { method: 'GET' }),
    {} as Feed
  )

  const hasVideos = computed(() => isDefined(videos) ? videos.value?.data.allVideos?.edges.length > 0 : false)

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
