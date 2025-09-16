<template>
  <section id="playlists" class="grid grid-cols-12 gap-2">
    <!-- Playlist Details -->
    <div class="col-span-4">
      <playlists-details v-if="showPlaylistDetails" @show:details="select" />
      <playlists-list v-else @show:create="openCreationDialog" @show:details="select" />
    </div>

    <!-- Videos -->
    <div class="col-span-8">
      <header>
        <VoltCard>
          <template #header>
            Select a playlist to display
          </template>
        </VoltCard>
      </header>

      <!-- Videos -->
      <div class="mt-5">
        <div v-if="hasVideos">
          <playlists-horizontal-video-card v-for="video in playlistVideos" :key="video.id" :video="video" />
        </div>
      </div>
    </div>

    <!-- Modals -->
    <client-only>
      <playlists-modals-create v-model="showCreatePlaylist" :playlists="playlists" :is-intelligent="isIntelligent" />
    </client-only> 
  </section>
</template>

<script setup lang="ts">
import { useCreatePlaylist } from '~/composables/use'

const showPlaylistDetails = ref<boolean>(false)

/**
 * Playlist
 */

const playlistStore = usePlaylistStore()
const { playlists } = storeToRefs(playlistStore)
playlistStore.fetch()

const playlistVideos = computed(() => currentPlaylist.value?.videos || [])
const hasVideos = computed(() => playlistVideos.value.length > 0)

/**
 * Edit
 */

const { showCreatePlaylist, select, openCreationDialog, currentPlaylist, isIntelligent } = useCreatePlaylist(playlists)

provide('playlists', playlists)
provide('currentPlaylist', currentPlaylist)
</script>
