<template>
  <div class="grid grid-cols-3 auto-rows-min gap-2">
    <article v-for="video in videos" :key="video.id" class="my-1">
      <NuxtLinkLocale :to="`/videos/${video.video_id}`">
        <VoltCard>
          <template #content>
            <VoltSkeleton height="200px" class="w-full" />

            <h1 class="font-bold mb-1">
              {{ video.title }}
            </h1>

            <p class="font-light">
              {{ video.user.get_full_name }}
            </p>
          </template>
        </VoltCard>
      </NuxtLinkLocale>
    </article>
  </div>

  <VoltCard>
    <template #content>
      <h2 class="text-center font-bold text-3xl">
        No videos
      </h2>
    </template>
  </VoltCard>
</template>

<script setup lang="ts">
import type { VideosFeedResponseData } from '~/types'

const emit = defineEmits<{ 'feed-loaded': [videos: VideosFeedResponseData[]] }>()

const feedStore = useFeedStore()
const { videos, hasVideos } = storeToRefs(feedStore)

const { data, status } = await useFetch<VideosFeedResponseData[]>('/api/videos', {
  method: 'GET',
  immediate: true
})

if (data.value) {
  videos.value = data.value || []
}

onMounted(() => {
  if (status.value === 'success') {
    emit('feed-loaded', videos.value)
  }
})
</script>
