<template>
  <div v-if="hasVideos" class="grid grid-cols-1 xl:grid-cols-5 auto-rows-min gap-2">
    <article v-for="video in data.data.allVideos.edges" :key="video.node.id" class="my-1">
      <u-card>
        <nuxt-link-locale :to="`/videos/${video.node.videoId}`">
          <volt-skeleton height="200px" class="w-full" />
        </nuxt-link-locale>

        <div class="mt-3">
          <nuxt-link-locale :to="`/channels/${video.node.userChannel.reference}`">
            <u-avatar :src="video.node.userChannel.user.userProfile.avatar" :alt="video.node.userChannel.name" shape="circle" />
          </nuxt-link-locale>

          <nuxt-link-locale :to="`/videos/${video.node.videoId}`">
            <h1 class="font-bold mt-2">
              {{ video.node.title }}
            </h1>
          </nuxt-link-locale>

          <p class="font-light text-sm mt-1">
            {{ video.node.userChannel.name }} . {{ shorten(video.node.views) }} views . <nuxt-time :datetime="video.node.createdOn" relative />
          </p>
        </div>
      </u-card>
    </article>
  </div>

  <u-card v-else class="shadow-sm">
    <h2 class="text-center font-bold text-4xl">
      No videos
    </h2>
  </u-card>
</template>

<script setup lang="ts">
const { shorten } = useNumbersUtils()

/**
 * Get Videos
 */

const { hasVideos, data } = await useSearchFeedComposable()
</script>
