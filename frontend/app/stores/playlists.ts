import type { Playlist } from '~/types'

/**
 * Composable for fetching playlists
 */
export const usePlaylistStore = defineStore('playlists', async () => {
  const playlists = ref<Playlist[]>([])

  if (playlists.value.length === 0) {
    const { data, execute } = useFetch<Playlist[]>('/playlists', {
      immediate: false
    })

    const debouncedExecute = useDebounceFn(execute, 3000)

    await debouncedExecute()

    if (data.value) {
      playlists.value.push(...data.value)
    }
  }

  return {
    /**
     * Reactive list of playlists
     */
    playlists
  }
})
