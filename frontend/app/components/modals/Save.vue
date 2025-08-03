<template>
  <VoltDialog id="save" v-model:open="show">
    <template #content>
      <VoltAutocomplete v-model="selectedPlaylistId" :suggestions="playlists" item-label="name" @search="search">
        <VoltInputText placeholder="Select a playlist" />
      </VoltAutocomplete>
    </template>

    <template #footer>
      <NuxtButton @click="() => show=false">
        Close
      </NuxtButton>

      <NuxtButton @click="() => add(selectedPlaylistId, $route.params.id)">
        Save
      </NuxtButton>
    </template>
  </VoltDialog>
</template>

<script setup lang="ts">
import { useEditPlaylists } from '~/composables/use'
import type { Playlist } from '~/types';

const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()

const selectedPlaylistId = ref(null)
const show = useVModel(props, 'modelValue', emit)

const playlistStore = usePlaylistStore()
const { playlists } = storeToRefs(playlistStore)

const { add } = useEditPlaylists(playlists)

const filteredPlaylists = ref<Playlist[]>([])
function search(event: CustomEvent<Event> & { query: string }) {
  filteredPlaylists.value = playlists.value.filter(item => {
    return item.name.toLowerCase().includes(event.query.toLowerCase())
  })
}
</script>
