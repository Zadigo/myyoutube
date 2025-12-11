<template>
  <volt-dialog v-model:visible="showCreatePlaylist" modal>
    <form @submit.prevent>
      <div class="space-y-2">
        <volt-input-text v-model="newPlaylist.name" placeholder="Name" class="w-full" />
        <volt-input-text v-model="newPlaylist.description" placeholder="Description" class="w-full" />

        <volt-label label-for="private" label="Private">
          <volt-toggle-switch v-model="newPlaylist.is_intelligent" />
        </volt-label>
      </div>

      {{ newPlaylist }}

      <div v-show="newPlaylist.is_intelligent" id="intelligent-functionnalities" class="mt-4">
        <div class="grid grid-cols-3 p-4 bg-primary-50 dark:bg-primary-900 rounded-md my-5">
          <volt-select :options="Array.from(intelligentVideoOptions)" />
          <volt-select placeholder="Operator" />
          <volt-input-text placeholder="Value" />
        </div>
      </div>
    </form>

    <volt-button @click="() => { toggleShowCreatePlaylist() }">
      Cancel
    </volt-button>

    <volt-button @click="async () => { await create(), toggleShowCreatePlaylist() }">
      Save
    </volt-button>
  </volt-dialog>
</template>

<script setup lang="ts">
/**
 * Creation
 */

const { playlists } = usePlaylistsComposable()
const { newPlaylist, create, intelligentVideoOptions, showCreatePlaylist, toggleShowCreatePlaylist } = useCreatePlaylist(playlists)
</script>
