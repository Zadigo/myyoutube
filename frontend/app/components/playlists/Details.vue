<template>
  <VoltCard>
    <template #body>
      <VoltAvatar image="/avatars/avatar1.png" shape="circle" />

      <VoltButton color="primary" class="mt-4" @click="emit('show:details', null)">
        <Icon name="i-fa7-solid:arrow-left" />
      </VoltButton>
      
      <VoltDivider class="my-5" />

      <div v-if="currentPlaylist">
        <h3>{{ currentPlaylist.name }}</h3>
        
        <p v-if="currentPlaylist.description" class="fw-light">
          {{ currentPlaylist.description }}
        </p>

        <p v-else class="">
          No description
        </p>
      </div>
    </template>
  </VoltCard>
</template>

<script setup lang="ts">
import type { Playlist } from '~/types'

const emit = defineEmits<{ 'show:details': [playlist: null] }>()

const currentPlaylist = inject<Ref<Playlist> | null>('currentPlaylist', null)
</script>
