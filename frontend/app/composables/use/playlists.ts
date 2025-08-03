import type { Playlist } from '~/types'

/**
 * Composable for editing playlists
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

export function editPlaylist(playlist: Playlist) {}
