<template>
  <section id="playlists" class="grid grid-cols-12 gap-2">
    <!-- Details -->
    <div class="col-span-4">
      <transition mode="out-in" enter-active-class="transition-all ease-in-out duration-200" leave-active-class="transition-all ease-in-out duration-200" enter-from-class="opacity-0 -translate-x-10" enter-to-class="opacity-100" leave-from-class="opacity-100" leave-to-class="opacity-0">
        <playlists-details v-if="showPlaylistDetails" />
        <playlists-list v-else @playlist:create="openCreationDialog" @playlist:details="select" />
      </transition>
    </div>

    <!-- Videos -->
    <div class="col-span-8">
      <header>
        <volt-card>
          <template #header>
            Select a playlist to display
          </template>
        </volt-card>
      </header>

      <!-- Videos -->
      <div class="mt-5">
        <div v-if="hasVideos">
          <playlists-horizontal-video-card v-for="video in playlistVideos" :key="video.node.id" :video="video" />
        </div>
      </div>
    </div>

    <!-- Modals -->
    <client-only>
      <playlists-modals-create :playlists="playlists" />
    </client-only> 
  </section>
</template>

<script setup lang="ts">
import { useCreatePlaylist } from '~/composables/use'

/**
 * Playlist
 */

const { playlists, select, getPlaylists, hasVideos, playlistVideos, showPlaylistDetails } = usePlaylistsComposable()
await getPlaylists()

/**
 * Edit
 */

const { openCreationDialog } = useCreatePlaylist(playlists)
</script>
