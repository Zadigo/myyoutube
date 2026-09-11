<template>
  <u-slideover v-model:open="showCreatePlaylist" modal>
    <template #body>
      <form @submit.prevent>
        <div class="space-y-2">
          <u-input v-model="newPlaylist.name" placeholder="Name" class="w-full" />
          <u-input v-model="newPlaylist.description" placeholder="Description" class="w-full" />
  
          <u-switch v-model="newPlaylist.is_intelligent" label="Private" />
        </div>
  
        {{ newPlaylist }}
  
        <div v-show="newPlaylist.is_intelligent" id="intelligent-functionnalities" class="mt-4">
          <div class="grid grid-cols-3 p-4 gap-2 bg-primary-50 dark:bg-slate-800 rounded-md my-5">
            <u-select :items="Array.from(INTELLIGENT_VIDEO_OPTIONS)" />
            <u-select :items="Array.from(GENERAL_CONDITIONS)" placeholder="Operator" />
            <u-input placeholder="Value" />
          </div>
        </div>
      </form>
    </template>

    <template #footer>
      <u-button @click="() => { toggleShowCreatePlaylist() }">
        Cancel
      </u-button>

      <u-button @click="async () => { await create(), toggleShowCreatePlaylist() }">
        Save
      </u-button>
    </template>
  </u-slideover>
</template>

<script setup lang="ts">
/**
 * Creation
 */

const { playlists } = usePlaylistsComposable()
const { newPlaylist, create, showCreatePlaylist, toggleShowCreatePlaylist } = useCreatePlaylist(playlists)
</script>
