<template>
  <u-modal id="save" v-model:open="showSaveModal" modal>
    <template #header>
      <h2 class="font-bold">
        Save to Playlist
      </h2>
    </template>

    <template #body>
      <form @submit.prevent>
        <u-input-menu v-model="selectedPlaylistId" :items="['a']" value-key="name" class="w-full" />
      </form>
    </template>

    <template #footer>
      <u-button icon="i-lucide-save" @click="() => add(selectedPlaylistId, $route.params.id)">
        Save
      </u-button>
    </template>
  </u-modal>
</template>

<script setup lang="ts">
/**
 * Modal
 */

const { showSaveModal } = useVideoDetailModalsStore()

/**
 * Playlists
 */

const selectedPlaylistId = ref<string>('')
const { playlists } = usePlaylistsComposable()

/**
 * Editionn
 */
  
const { add } = useEditPlaylistsComposable(playlists)
</script>
