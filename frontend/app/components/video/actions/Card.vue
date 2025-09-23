<template>
  <volt-card>
    <template #content>
      <client-only>
        <div v-if="currentVideo">
          <h1 class="font-bold text-2xl">
            {{ currentVideo.title }}
          </h1>
        </div>
        <volt-skeleton v-else height="50px" />

        <div v-if="currentVideo" class="flex justify-between items-center mt-3">
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
        <volt-skeleton v-else height="50px" />
      </client-only>
    </template> 
  </volt-card>
</template>

<script lang="ts" setup>
import type { DefaultVideoMenuActions } from '~/data'
import type { BaseVideo } from '~/types'

const emit = defineEmits<{ action: [method: DefaultVideoMenuActions] }>()

const currentVideo = inject<BaseVideo>('currentVideo')

onMounted(() => {
  const playlistsStore = usePlaylistStore()
  playlistsStore.fetch()
})
</script>
