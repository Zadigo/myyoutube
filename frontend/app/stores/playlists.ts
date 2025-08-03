import type { Playlist } from '~/types'
import { playlistsFixture } from '~/data/fixtures'

/**
 * Composable for fetching playlists
 */
export const usePlaylistStore = defineStore('playlists', () => {
  const playlists = ref<Playlist[]>([])

  const hasPlaylists = computed(() => playlists.value.length > 0)

  async function fetch() {
    if (playlists.value.length === 0) {
      // const { data, execute } = useFetch<Playlist[]>('/v1/playlists', {
      //   method: 'GET',
      //   baseURL: useRuntimeConfig().public.djangoProdUrl,
      //   immediate: false,
      //   lazy: true,
      //   onRequestError({ response }) {
      //     if (response) {
      //       if (response.status === 401) {
      //         refreshAccessTokenClient()
      //       }
      //     }
      //   }
      // })
  
      // await useDebounceFn(execute, 3000)()

  
      // if (data.value) {
      //   playlists.value.push(...data.value)

      //   // TODO: Save to firebase
      // }

      playlists.value = playlistsFixture
    }
  }

  const search = ref<string>('')
  const searched = computed(() => {
    if (!search.value) {
      return playlists.value
    } else {
      return playlists.value.filter(item => {
        return item.name.toLowerCase().includes(search.value.toLowerCase())
      })
    }
  })

  return {
    /**
     * Fetch playlists if not already fetched
     */
    fetch,
    /**
     * Reactive list of playlists
     */
    playlists,
    /**
     * Search term for filtering playlists
     */
    search,
    /**
     * Filtered list of playlists based on search term
     */
    searched,
    /**
     * Reactive boolean indicating if there are videos in the playlists
     */
    hasPlaylists
  }
})
