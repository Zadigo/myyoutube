<template>
  <volt-card v-if="currentVideo">
    <template #content>
      <h1 class="font-bold text-2xl">
        {{ currentVideo.title }}
      </h1>

      <div class="flex justify-between items-center mt-3">
        <div v-if="currentVideo.user_channel" id="left" class="flex justify-left items-center gap-3">
          <nuxt-link :to="`/channels/${currentVideo.user_channel?.reference}`">
            <volt-avatar image="/avatars/avatar1.png" size="xlarge" shape="circle" alt="" />
          </nuxt-link>
          
          <div class="wrapper">
            <h3 class="font-bold mb-1">
              103M views
            </h3>

            <p class="font-light text-secondary">
              20 months ago
            </p>
          </div>
        </div>

        <video-actions-buttons @action="emit('action', $event)" />
      </div>
    </template> 
  </volt-card>

  <volt-card v-else>
    <template #content>
      <div class="space-y-2">
        <volt-skeleton height="50px" />
        <volt-skeleton height="50px" />
      </div>
    </template>
  </volt-card>
</template>

<script lang="ts" setup>
import { currentVideoSymbol, type DefaultVideoMenuActions } from '~/data'
import type { BaseVideo, Undefineable } from '~/types'

const emit = defineEmits<{ action: [method: DefaultVideoMenuActions] }>()

const currentVideo = injectLocal<Ref<Undefineable<BaseVideo>>>(currentVideoSymbol)

onMounted(() => {
  const playlistsStore = usePlaylistStore()
  playlistsStore.fetch()
})
</script>
