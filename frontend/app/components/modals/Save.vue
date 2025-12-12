<template>
  <volt-dialog id="save" v-model:visible="showSaveModal" modal>
    <template #header>
      <h2 class="font-bold">
        Save to Playlist
      </h2>
    </template>

    <form @submit.prevent>
      <volt-autocomplete v-model="selectedPlaylistId" :suggestions="filteredPlaylists" option-label="name" dropdown @complete="handleSearch" />
    </form>

    <template #footer>
      <volt-button @click="() => add(selectedPlaylistId, $route.params.id)">
        Save
      </volt-button>
    </template>
  </volt-dialog>
</template>

<script setup lang="ts">
import { useEditPlaylists } from '~/composables/use'
import type { Playlist } from '~/types'

/**
 * Modal
 */

const { showSaveModal } = tryUseVideoDetailModalsStore()

/**
 * Playlists
 */

const selectedPlaylistId = ref<string | null>(null)
const { playlists } = usePlaylistsComposable()

const playlistMenuItems = computed(() => playlists.value.map(item => ({ name: item.name })))
  
const { add } = useEditPlaylists(playlists)
const filteredPlaylists = ref<Playlist[]>([])

function handleSearch(event: CustomEvent<Event> & { query: string }) {
  filteredPlaylists.value = playlists.value.filter(item => {
    return item.name.toLowerCase().includes(event.query.toLowerCase())
  })
}
</script>
