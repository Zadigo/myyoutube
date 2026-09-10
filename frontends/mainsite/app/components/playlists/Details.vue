<template>
  <u-card>
    <u-avatar src="/avatars/avatar1.png" />

    <u-button color="primary" class="mt-4" @click="() => { toggleShowPlaylistDetails() }">
      <icon name="lucide:arrow-left" />
    </u-button>
    
    <u-separator class="my-5" />

    <div v-if="currentPlaylist">
      <h3>{{ currentPlaylist.name }}</h3>
      <p v-if="currentPlaylist.description" class="font-light">{{ currentPlaylist.description }}</p>
      <p v-else class="font-light">No description provided.</p>
    </div>
 </u-card>
</template>

<script setup lang="ts">
const { currentPlaylist, toggleShowPlaylistDetails } = usePlaylistsComposable()
</script>
