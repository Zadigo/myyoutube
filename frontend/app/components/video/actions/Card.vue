<template>
  <VoltCard>
    <template #content>
      <ClientOnly>
        <div v-if="currentVideo">
          <h1 class="font-bold text-2xl">
            {{ currentVideo.title }}
          </h1>
        </div>
        <VoltSkeleton v-else height="50px" />

        <div v-if="currentVideo" class="flex justify-between items-center mt-3">
          <div v-if="currentVideo.user_channel" id="left" class="flex justify-left items-center gap-3">
            <NuxtLink :to="`/channels/${currentVideo.user_channel?.reference}`">
              <VoltAvatar image="/avatars/avatar1.png" size="xlarge" shape="circle" alt="" />
            </NuxtLink>
            
            <div class="wrapper">
              <h3 class="font-bold mb-1">
                103M views
              </h3>

              <p class="font-light text-secondary">
                20 months ago
              </p>
            </div>
          </div>

          <VideoActionsButtons @action="emit('action', $event)" />
        </div>
        <VoltSkeleton v-else height="50px" />
      </ClientOnly>
    </template> 
  </VoltCard>
</template>

<script lang="ts" setup>
import type { DefaultVideoMenuActions } from '~/data';
import type { VideoInfo } from '~/types';

const emit = defineEmits<{ action: [method: DefaultVideoMenuActions] }>()

const currentVideo = inject<VideoInfo>('currentVideo')

onMounted(() => {
  const playlistsStore = usePlaylistStore()
  playlistsStore.fetch()
})
</script>
