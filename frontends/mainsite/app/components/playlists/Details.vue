<template>
  <u-card>
    <u-button variant="subtle" class="mt-4" @click="() => { toggleShowPlaylistDetails() }">
      <icon name="lucide:arrow-left" />
    </u-button>

    <div class="overflow-hidden rounded-lg">
      <nuxt-img src="/avatars/avatar1.png" class="w-full h-full hover:scale-105 hover:opacity-95 transition-all duration-300" alt="" />
    </div>

    <u-separator class="my-5" />

    <div v-if="currentPlaylist">
      <h3 class="text-lg font-bold">{{ currentPlaylist.node.name }}</h3>
      <p v-if="currentPlaylist.node.description" class="text-sm font-light">
        {{ currentPlaylist.node.description }}
      </p>
      <p v-else class="text-sm font-light">
        No description provided.
      </p>
    </div>
 </u-card>
</template>

<script setup lang="ts">
const { currentPlaylist, toggleShowPlaylistDetails } = usePlaylistsComposable()
</script>
