<template>
  <volt-card>
    <template #content>
      <volt-avatar image="/avatars/avatar1.png" shape="circle" />

      <volt-button color="primary" class="mt-4" @click="() => { toggleShowPlaylistDetails() }">
        <icon name="lucide:arrow-left" />
      </volt-button>
      
      <volt-divider class="my-5" />

      <div v-if="currentPlaylist">
        <h3>{{ currentPlaylist.name }}</h3>
        <p v-if="currentPlaylist.description" class="font-light">{{ currentPlaylist.description }}</p>
        <p v-else class="font-light">No description provided.</p>
      </div>
    </template>
  </volt-card>
</template>

<script setup lang="ts">
const { currentPlaylist, toggleShowPlaylistDetails } = usePlaylistsComposable()
</script>
