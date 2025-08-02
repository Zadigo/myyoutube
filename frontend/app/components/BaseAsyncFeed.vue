<template>
  <div v-if="hasVideos" class="grid grid-cols-3 auto-rows-min gap-2">
    <article v-for="video in videos" :key="video.id" class="my-1">
      <NuxtLinkLocale :to="`/videos/${video.video_id}`">
        <VoltCard>
          <NuxtSkeleton class="h-[200px]" />

          <h1 class="font-bold mb-1">
            {{ video.title }}
          </h1>

          <p class="font-light">
            {{ video.user.get_full_name }}
          </p>
        </VoltCard>
      </NuxtLinkLocale>
    </article>
  </div>

  <div v-else class="row">
    <VoltCard>
      <template #content>
        <h2 class="text-center font-bold text-3xl">
          No videos
        </h2>
      </template>
    </VoltCard>
  </div>
</template>

<script setup lang="ts">
import type { VideosFeedResponseData } from '~/types'

const emit = defineEmits<{ 'feed-loaded': [videos: VideosFeedResponseData[]] }>()

const feedStore = useFeed()
const { videos, hasVideos } = storeToRefs(feedStore)

const { data } = await useFetch<VideosFeedResponseData[]>('/api/feed', {
  method: 'GET',
  baseURL: useRuntimeConfig().public.djangoProdUrl,
  immediate: true
})

if (data) {
  videos.value = data.value || []
}

onMounted(() => {
  emit('feed-loaded', videos.value)
})
</script>
