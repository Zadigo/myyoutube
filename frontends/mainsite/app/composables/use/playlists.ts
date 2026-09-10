import { playlistsFixture } from '~/utils/fixtures'

/**
 * Composable for editing playlists
 * @param playlists Reactive reference to the list of playlists
 */
export function useEditPlaylistsComposable(_playlists: MaybeRefOrGetter<Arrayable<RelayNode<SinglePlaylist>>>) {
  if (import.meta.server) {
    return {
      add: async () => {},
      remove: async () => {}
    }
  }

  async function add(playlistId: Nullable<string>, videoId: Undefineable<string> | string[]) {
    return await $fetch(`/api/playlists/${playlistId}/add`, {
      method: 'POST',
      baseURL: useRuntimeConfig().public.djangoProdUrl,
      body: { video_id: videoId }
    })
  }

  async function remove(playlistId: string, videoId: string) {
    return await $fetch(`/api/playlists/${playlistId}/remove`, {
      method: 'POST',
      baseURL: useRuntimeConfig().public.djangoProdUrl,
      body: { video_id: videoId }
    })
  }

  return {
    /**
     * Add a video to a playlist
     * @param playlistId The ID of the playlist to add the video to
     * @param videoId The ID of the video to add to the playlist
     */
    add,
    /**
     * Remove a video from a playlist
     * @param playlistId The ID of the playlist to remove the video from
     * @param videoId The ID of the video to remove from the playlist
     */
    remove
  }
}

/**
 * Composable for creating and managing playlists
 * @param playlists Reactive reference to the list of playlists
 */
export const useCreatePlaylist = createSharedComposable((_playlists: MaybeRefOrGetter<Arrayable<RelayNode<SinglePlaylist>>>) => {
  /**
   * Creation Dialog
   */

  const [showCreatePlaylist, toggleShowCreatePlaylist] = useToggle<boolean>(false)

  /**
   * Creation
   */

  const newPlaylist = ref<NewPlaylist>({
    name: '',
    description: '',
    is_intelligent: false
  })

  function openCreationDialog(intelligent = false) {
    console.log('Opening creation dialog for intelligent:', intelligent)
    newPlaylist.value.is_intelligent = intelligent
    toggleShowCreatePlaylist()
  }

  async function create() {
    return $fetch<Playlist>('/api/playlists/create', { 
      method: 'POST', 
      body: newPlaylist.value 
    })
  }

  /**
   * Intelligent playlist
   */

  const intelligentVideoOptions = [
    'Name',
    'Author',
    'Release Date'
  ] as const

  return {
    /**
     * Options for intelligent video filtering
     */
    intelligentVideoOptions,
    /**
     * Reactive reference to the new playlist being created
     */
    newPlaylist,
    /**
     * Whether to show the create playlist dialog or not
     */
    showCreatePlaylist,
    /**
     * Open the creation dialog
     * @param [intelligent=false] Whether the playlist is intelligent or not
     */
    openCreationDialog,
    /**
     * Create a new playlist
     * @param [intelligent=false] Whether the playlist is intelligent or not 
     */
    create,
    /**
     * Toggle the visibility of the create playlist dialog
     */
    toggleShowCreatePlaylist
  }
})

/**
 * Global state composable for playlists
 */
export const usePlaylistsComposable = createGlobalState(() => {
  const _playlists = ref<Playlist>()
  const playlists = computed(() => _playlists.value?.data.allplaylists.edges || [])

  async function getPlaylists() {
    await $fetch('/api/playlists', { method: 'GET' })
    _playlists.value = playlistsFixture
  }

  /**
   * Currently selected playlist
   */

  const currentPlaylist = ref<RelayNode<SinglePlaylist>>()
  const query = useUrlSearchParams() as { playlist: string }

  const [showPlaylistDetails, toggleShowPlaylistDetails] = useToggle<boolean>(false)
  
  function select(item: RelayNode<SinglePlaylist>) {
    if (isDefined(item)) {
      currentPlaylist.value = item
      query.playlist = item.node.playlistId
      toggleShowPlaylistDetails(true)
    }
  }

  /**
   * Videos
   */

  const playlistVideos = computed(() => currentPlaylist.value?.node.videos.edges)
  const hasVideos = computed(() => isDefined(playlistVideos) ? playlistVideos.value.length > 0 : false)
  
  /**
   * Search
   */
  
  const search = ref<string>('')

  const searched = computed(() => {
    if (!search.value) {
      return playlists.value
    } else {
      return playlists.value.filter(item => {
        return item.node.name.toLowerCase().includes(search.value.toLowerCase())
      })
    }
  })

  return {
    currentPlaylist,
    playlists,
    searched,
    playlistVideos,
    hasVideos,
    showPlaylistDetails,
    toggleShowPlaylistDetails,
    select,
    getPlaylists
  }
})
