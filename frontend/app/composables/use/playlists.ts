import type { Arrayable, Nullable, Playlist, Refeable } from '~/types'

/**
 * Composable for editing playlists
 * @param playlists Reactive reference to the list of playlists
 */
export function useEditPlaylists(playlists: Refeable<Arrayable<Playlist>>) {
  async function add(playlistId: string, videoId: string) {
    const data = await $fetch(`/playlists/${playlistId}/add`, {
      method: 'POST',
      baseURL: useRuntimeConfig().public.djangoProdUrl,
      body: { video_id: videoId }
    })

    if (data) {
      // Do something
    }
  }

  async function remove(playlistId: string, videoId: string) {
    await $fetch(`/playlists/${playlistId}/remove`, {
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
    add
    /**
     * Remove a video from a playlist
     * @param playlistId The ID of the playlist to remove the video from
     * @param videoId The ID of the video to remove from the playlist
     */
    ,
    remove
  }
}

export interface NewPlaylist {
  name: Nullable<string>
  description: Nullable<string>
  is_intelligent: boolean
}

/**
 * Composable for creating and managing playlists
 * @param playlists Reactive reference to the list of playlists
 */
export function useCreatePlaylist(playlists: Ref<Playlist[]>) {
  const showCreatePlaylist = ref<boolean>(false)
  const isIntelligent = ref<boolean>(false)

  function openCreationDialog(intelligent: boolean = false) {
    isIntelligent.value = intelligent
    showCreatePlaylist.value = true
  }

  /**
   * Create
   */

  const newPlaylist = ref<NewPlaylist>({
    name: null,
    description: null,
    is_intelligent: false
  })

  async function create(intelligent: boolean = false) {
    const data = await $fetch<Playlist>('/playlists/create', {
      method: 'POST',
      body: newPlaylist.value,
      onResponse({ response }) {
        if (response.status === 201) {
          showCreatePlaylist.value = false
          
          newPlaylist.value = {
            name: null,
            description: null,
            is_intelligent: intelligent
          }
        }
      }
    })

    playlists.value.push(data)
  }

  watch(showCreatePlaylist, (n) => {
    if (!n) {
      isIntelligent.value = false
    }
  })

  /**
   * Currently selected playlist
   */

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
    /**
     * Select a playlist to view/edit
     */
    select,
    /**
     * Create a new playlist
     * @param [intelligent=false] Whether the playlist is intelligent or not 
     */
    create
  }
}
