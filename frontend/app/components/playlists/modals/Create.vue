<template>
  <volt-dialog v-model:visible="show" modal>
    <form @submit.prevent>
      <div class="space-y-2">
        <volt-input-text v-model="newPlaylist.name" placeholder="Name" class="w-full" />
        <volt-input-text v-model="newPlaylist.description" placeholder="Description" class="w-full" />

        <volt-label>
          <volt-toggle-switch v-model="newPlaylist.is_intelligent" />
          <label>Private</label>
        </volt-label>
      </div>

      <div v-show="isIntelligent" id="intelligent-functionnalities" class="mt-4">
        <div class="flex gap-2 p-4 bg-slate-50 rounded-md my-5">
          <volt-select :options="Array.from(intelligentVideoOptions)" />
          <volt-select placeholder="Operator" />
          <volt-input-text placeholder="Value" />
        </div>
      </div>
    </form>

    <volt-button @click="() => { show = false }">
      Cancel
    </volt-button>

    <volt-button @click="create">
      Save
    </volt-button>
  </volt-dialog>
</template>

<script setup lang="ts">
import { useCreatePlaylist } from '~/composables/use'
import type { Playlist } from '~/types'

const props = defineProps<{ modelValue: boolean, playlists: Ref<Playlist[]>, isIntelligent: boolean }>()
const emit = defineEmits<{ 'update:modelValue': boolean }>()
const show = useVModel(props, 'modelValue', emit)

/**
 * Creation
 */

const playlistStore = usePlaylistStore()
const { playlists } = storeToRefs(playlistStore)

const { isIntelligent, newPlaylist, create, intelligentVideoOptions } = useCreatePlaylist(playlists)
</script>
