import type { DefaultMainCategories, DefaultSortBy, DefaultUploadDate, DefaultVideoLength } from '~/data'
import type { BaseVideo } from '~/types'

export function useSearchFeedComposable() {
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

  const query = useUrlSearchParams() as {
    search?: string
    category?: DefaultMainCategories
    videoLength?: DefaultVideoLength
    uploadDate?: DefaultUploadDate
    sortBy?: DefaultSortBy
  }

  watch([search, category, videoLength, uploadDate, sortBy], (newValues) => {
    const [newSearch, newCategory, newVideoLength, newUploadDate, newSortBy] = newValues

    query.search = newSearch || undefined
    query.category = newCategory !== 'All' ? newCategory : undefined
    query.videoLength = newVideoLength !== '4-20 minutes' ? newVideoLength : undefined
    query.uploadDate = newUploadDate !== 'This week' ? newUploadDate : undefined
    query.sortBy = newSortBy !== 'Upload date' ? newSortBy : undefined
  })

  return {
    search,
    category,
    videoLength,
    uploadDate,
    sortBy
  }
}


export const useFeedComposable = createSharedComposable(async () => {
  const { search, category, videoLength, uploadDate, sortBy } = useSearchFeedComposable()

  /**
   * Request
   */

  const { data, execute } = await useFetch<BaseVideo[]>('/api/videos', {
    method: 'GET',
    immediate: false,
    watch: [search, category, videoLength, uploadDate, sortBy],
    key: `videos-feed-${search.value}-${category.value}-${videoLength.value}-${uploadDate.value}-${sortBy.value}`
  })

  const videos = refDefault<BaseVideo[]>(data, [])
  const hasVideos = computed(() => videos.value.length > 0)

  console.log('Videos:', videos.value, data.value, hasVideos.value)

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
