import type { DefaultMainCategories, DefaultSortBy, DefaultUploadDate, DefaultVideoLength } from "~/data"
import type { VideosFeedResponseData } from "~/types"

export const useFeedComposable = createSharedComposable(async () => {
  /**
   * Search
   */

  const search = ref<string>('')
  const category = ref<DefaultMainCategories>('All')
  const videoLength = ref<DefaultVideoLength>('4-20 minutes')
  const uploadDate = ref<DefaultUploadDate>('This week')
  const sortBy = ref<DefaultSortBy>('Upload date')

  /**
   * Request
   */

  const { data, execute } = await useFetch<VideosFeedResponseData[]>('/api/videos', {
    method: 'GET',
    immediate: false,
    watch: [search, category, videoLength, uploadDate, sortBy],
    key: `videos-feed-${search.value}-${category.value}-${videoLength.value}-${uploadDate.value}-${sortBy.value}`
  })

  const videos = refDefault<VideosFeedResponseData[]>(data, [])
  const hasVideos = computed(() => videos.value.length > 0)

  console.log('Videos:', videos.value, data.value, hasVideos.value)

  // watchDebounced([refresh], async () => {
  //   await refresh()
  // }, {
  //   immediate: false,
  //   debounce: 500
  // })

  return {
    execute,
    /**
     * The search query
     * @default ""
     */
    search,
    /**
     * The category to filter videos by
     * @default 'All'
     */
    category,
    /**
     * How long the videos should be
     * @default 'This week'
     */
    videoLength,
    /**
     * The upload date to filter videos by
     * @default 'This week'
     */
    uploadDate,
    /**
     * How to sort the videos
     * @default 'Upload date'
     */
    sortBy,
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
