<template>
  <VoltDialog id="save" v-model:visible="show" modal>
    <template #header>
      <h2 class="font-bold">
        Save to Playlist
      </h2>
    </template>

    <form @submit.prevent>
      <VoltAutoComplete v-model="selectedPlaylistId" :suggestions="filteredPlaylists" option-label="name" dropdown @complete="handleSearch" />
    </form>

    <template #footer>
      <VoltButton @click="() => add(selectedPlaylistId, $route.params.id)">
        Save
      </VoltButton>
    </template>
  </VoltDialog>
</template>

<script setup lang="ts">
import { useEditPlaylists } from '~/composables/use'

import type { Playlist } from '~/types';

const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })

const selectedPlaylistId = ref<string | null>(null)

const playlistStore = usePlaylistStore()
const { playlists } = storeToRefs(playlistStore)

const playlistMenuItems = computed(() => playlists.value.map(item => ({ name: item.name })))

const { add } = useEditPlaylists(playlists)

const filteredPlaylists = ref<Playlist[]>([])

function handleSearch(event: CustomEvent<Event> & { query: string }) {
  filteredPlaylists.value = playlists.value.filter(item => {
    return item.name.toLowerCase().includes(event.query.toLowerCase())
  })
}
</script>
