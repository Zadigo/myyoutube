import type { Playlist } from '~/types'

/**
 * Composable for editing playlists
 * @param playlists Reactive reference to the list of playlists
 */
export function useEditPlaylists(playlists: Ref<Playlist[]> = ref([])) {
  const availablePlaylists = computed(() => playlists.value)

  async function add(playlistId: string, videoId: string) {
    const { data } = await useAsyncData(`/playlists/${playlistId}/add`, () => {
      return useFetch(`/playlists/${playlistId}/add`, {
        method: 'POST',
        baseURL: useRuntimeConfig().public.djangoProdUrl,
        body: { video_id: videoId }
      })
    }, {
      immediate: true
    })

    if (data.value) {
      return
    }
  }

  return {
    /**
     * Add a video to a playlist
     * @param playlistId The ID of the playlist to add the video to
     * @param videoId The ID of the video to add to the playlist
     */
    add
  }
}

export interface NewPlaylist {
  name: string | null
  description: string | null
  is_intelligent: boolean
}

/**
 * Composable for creating and managing playlists
 * @param playlists Reactive reference to the list of playlists
 */
export function useEditPlaylist(playlists: Ref<Playlist[]>) {
  const showCreatePlaylist = ref<boolean>(false)
  const isIntelligent = ref<boolean>(false)

  function openCreationDialog(intelligent: boolean = false) {
    isIntelligent.value = intelligent
    showCreatePlaylist.value = true
  }

  const newPlaylist = ref<NewPlaylist>({
    name: null,
    description: null,
    is_intelligent: false
  })

  /**
   * Create a new playlist
   * @param [intelligent=false] Whether the playlist is intelligent or not 
   */
  async function create(intelligent: boolean = false) {
    try {
      const response = await $fetch<Playlist>('/playlists/create', {
        method: 'POST',
        body: newPlaylist.value,
      })

      playlists.value.push(response)

      showCreatePlaylist.value = false

      newPlaylist.value = {
        name: null,
        description: null,
        is_intelligent: intelligent
      }
    } catch (e) {
      console.error(e)
    }
  }

  watch(showCreatePlaylist, (n) => {
    if (!n) {
      isIntelligent.value = false
    }
  })

  const currentPlaylist = ref<Playlist>()

  function select(playlist: Playlist) {
    currentPlaylist.value = playlist
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
    intelligentVideoOptions,
    currentPlaylist,
    newPlaylist,
    showCreatePlaylist,
    isIntelligent,
    openCreationDialog,
    select,
    create
  }
}
