<template>
  <div v-if="hasVideos" class="grid grid-cols-1 xl:grid-cols-3 auto-rows-min gap-2">
    <article v-for="video in videos" :key="video.id" class="my-1">
      <nuxt-link-locale :to="`/videos/${video.video_id}`">
        <volt-card class="shadow-sm">
          <template #content>
            <volt-skeleton height="200px" class="w-full" />

            <div class="mt-3">
              <volt-avatar :image="video.user_channel.avatar" :alt="video.user_channel.name" shape="circle" />

              <h1 class="font-bold mt-2">
                {{ video.title }}
              </h1>

              <p class="font-light text-sm mt-1">
                {{ video.user_channel.name }} . 25 views . {{ new Date(video.created_on).toLocaleDateString() }}
              </p>
            </div>
          </template>
        </volt-card>
      </nuxt-link-locale>
    </article>
  </div>

  <volt-card v-else class="shadow-sm">
    <template #content>
      <h2 class="text-center font-bold text-4xl">
        No videos
        {{ videos }}
      </h2>
    </template>
  </volt-card>
</template>

<script setup lang="ts">
/**
 * Get Videos
 */

const { hasVideos, videos, execute } = await useFeedComposable()
await execute()
</script>
