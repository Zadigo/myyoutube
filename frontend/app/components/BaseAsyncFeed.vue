<template>
  <div v-if="hasVideos" class="grid grid-cols-1 xl:grid-cols-5 auto-rows-min gap-2">
    <article v-for="video in videos" :key="video.id" class="my-1">
      <volt-card class="shadow-sm">
        <template #content>
          <nuxt-link-locale :to="`/videos/${video.videoId}`">
            <volt-skeleton height="200px" class="w-full" />
          </nuxt-link-locale>

          <div class="mt-3">
            <nuxt-link-locale :to="`/channels/${video.userChannel.reference}`">
              <volt-avatar :image="video.user.userProfile.avatar" :alt="video.userChannel.name" shape="circle" />
            </nuxt-link-locale>

            <nuxt-link-locale :to="`/videos/${video.videoId}`">
              <h1 class="font-bold mt-2">
                {{ video.title }}
              </h1>
            </nuxt-link-locale>

            <p class="font-light text-sm mt-1">
              {{ video.userChannel.name }} . {{ shorten(video.views) }} views . {{ $humanizeDate(video.createdOn) }}
            </p>
          </div>
        </template>
      </volt-card>
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
const { shorten } = useNumbersUtils()

/**
 * Date
 */

const { $humanizeDate } = useNuxtApp()

/**
 * Get Videos
 */

const { hasVideos, videos, execute } = await useFeedComposable()
await execute()
</script>
