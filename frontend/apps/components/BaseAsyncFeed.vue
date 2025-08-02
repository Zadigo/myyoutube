<template>
  <div v-if="hasVideos" class="row">
    <div v-for="video in videos" :key="video.id" class="col-3 my-1">
      <NuxtLink :to="`/videos/${video.video_id}`" :data-id="video.video_id">
        <article class="card shadow-sm" :aria-label="video.title">
          <BaseSkeleton :loading="true" height="100px" />

          <div class="card-body">
            <h1 class="h5 fw-bold card-title mb-1">
              {{ video.title }}
            </h1>

            <p class="fw-light">
              {{ video.user.get_full_name }}
            </p>
          </div>
        </article>
      </NuxtLink>
    </div>
  </div>

  <div v-else class="row">
    <h2 class="text-center fw-bold">
      No videos
    </h2>
  </div>
</template>

<script setup lang="ts">
import type { VideoInfo } from '~/apps/types'

import { useFeed } from '~/apps/stores/feed';
import { storeToRefs } from 'pinia';

const emit = defineEmits({
'feed-loaded' (_videos: VideoInfo[]) {
    return true
  }
})

const { client } = useAxiosClient()
const feedStore = useFeed()
const { videos, hasVideos } = storeToRefs(feedStore)

async function requestVideos () {
  try {
    const response = await client.get<VideoInfo[]>('/videos/')
    feedStore.videos = response.data
  } catch (e) {
    // Handle error
    console.log(e)
  }
}

await requestVideos()

onMounted(() => {
  emit('feed-loaded', videos.value)
})
</script>
