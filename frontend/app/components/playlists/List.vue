<template>
  <VoltCard>
    <template #content>
      <VoltButton class="me-2" color="primary" size="small" @click="emit('show:create', false)">
        <Icon name="i-fa7-solid:plus" class="me-2" />
        Playlist
      </VoltButton>

      <VoltButton variant="outlined" color="primary" size="small" @click="emit('show:create', true)">
        <Icon name="i-fa7-solid:star" class="me-2" />
        Intelligent playlist
      </VoltButton>

      <VoltDivider class="my-3" />

      <div class="space-y-2">
        <a v-for="playlist in playlists" :key="playlist.id" href="#" class="bg-primary-50 hover:bg-primary-100 dark:bg-primary-800 dark:hover:bg-primary-700 block rounded-lg p-3" @click.prevent="emit('show:details', playlist)">
          <article :data-id="playlist.id">
            <p class="font-bold">{{ playlist.name }}</p>
            <p v-if="playlist.description" class="font-light m-0">
              {{ playlist.description }}
            </p>
          </article>
        </a>
      </div>
    </template>
  </VoltCard>
</template>

<script setup lang="ts">
import type { Playlist } from '~/types'

const emit = defineEmits<{ 'show:create': [intelligent: boolean], 'show:details': [playlist: Playlist] }>()

const playlists = inject<Playlist[]>('playlists', [])
</script>
