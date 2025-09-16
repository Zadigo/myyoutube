<template>
  <div v-if="hasVideos" class="grid grid-cols-3 auto-rows-min gap-2">
    <article v-for="video in videos" :key="video.id" class="my-1">
      <NuxtLinkLocale :to="`/videos/${video.video_id}`">
        <VoltCard class="shadow-sm">
          <template #content>
            <VoltSkeleton height="200px" class="w-full" />

            <div class="mt-3">
              <VoltAvatar :image="video.user_channel.avatar" :alt="video.user_channel.name" shape="circle" />

              <h1 class="font-bold">
                {{ video.title }}
              </h1>

              <p class="font-light">
                {{ video.user_channel.name }} . 25 views . {{ new Date(video.created_on).toLocaleDateString() }}
              </p>
            </div>
          </template>
        </VoltCard>
      </NuxtLinkLocale>
    </article>
  </div>

  <VoltCard v-else class="shadow-sm">
    <template #content>
      <h2 class="text-center font-bold text-4xl">
        No videos
      </h2>
    </template>
  </VoltCard>
</template>

<script setup lang="ts">
import type { VideosFeedResponseData } from '~/types'

const feedStore = useFeedStore()
const { videos, hasVideos } = storeToRefs(feedStore)

const { data } = await useFetch<VideosFeedResponseData[]>('/api/videos', {
  method: 'GET',
  immediate: true
})

if (data.value) {
  videos.value = data.value || []
}

console.log(videos.value)
</script>
