<template>
  <v-dialog id="save" v-model="show" width="400" persistent>
    <v-card>
      <v-card-text>
        <v-autocomplete v-model="selectedPlaylistId" :items="playlists"  item-title="title" item-value="playlist_id" clearable auto-select-first>
          <VoltInputText placeholder="Select a playlist" />
        </v-autocomplete>
      </v-card-text>

      <v-card-actions>
        <v-btn @click="show=false">
          Close
        </v-btn>

        <v-btn @click="requestSaveToPlaylist">
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import type { Playlist } from '~/apps/types'

const emit = defineEmits({
  'update:modelValue' (_value: boolean) {
    return true
  }
})

const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true
  },
  playlists: {
    type: Object as PropType<Playlist[]>,
    required: true
  }
})

const { $client } = useNuxtApp()

const selectedPlaylistId = ref(null)

const show = computed({
  get: () => props.modelValue,
  set: (value) => {
    emit('update:modelValue', value)
  }
})

// Function that saves the current video
// to the given playlist
async function requestSaveToPlaylist () {
  try {
    await $client.post(`/playlists/${selectedPlaylistId.value}/add`, {
      video: route.params.id
    })
  } catch (e) {
    console.error('requestSaveToPlaylist', e)
  }
}
</script>
