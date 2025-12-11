<template>
  <volt-card>
    <template #content>
      <volt-button class="me-2" size="small" @click="emit('playlist:create', false)">
        <icon name="lucide:plus" class="me-2" />
        Playlist
      </volt-button>

      <volt-button size="small" @click="emit('playlist:create', true)">
        <icon name="lucide:star" class="me-2" />
        Intelligent playlist
      </volt-button>

      <volt-divider class="my-3" />

      <div class="space-y-2">
        <a v-for="playlist in playlists" :key="playlist.id" href="#" class="bg-primary-50 hover:bg-primary-100 dark:bg-primary-900 dark:hover:bg-primary-800 block rounded-lg p-3" @click.prevent="emit('playlist:details', playlist)">
          <article :data-id="playlist.id">
            <p class="font-bold">{{ playlist.name }}</p>
            <p v-if="playlist.description" class="font-light m-0">
              {{ playlist.description }}
            </p>
          </article>
        </a>
      </div>
    </template>
  </volt-card>
</template>

<script setup lang="ts">
import type { Playlist } from '~/types'

const emit = defineEmits<{ 'playlist:create': [intelligent: boolean], 'playlist:details': [playlist: Playlist] }>()

const { playlists } = usePlaylistsComposable() 
</script>
