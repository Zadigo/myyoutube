<template>
  <section id="video-details">
    <!-- Video -->
    <section id="video-player">
      <client-only>
        <video-player-overlay>
          <video-player-base :video-source="videoSource" @update:metadata="handleLoadedMetaData" />
        </video-player-overlay>
      </client-only>
    </section>

    <!-- Actions -->
    <section id="information" class="mt-4">
      <lazy-video-actions-card hydrate-on-idle @action:modal="openModal" />
    </section>
    
    <section class="grid grid-cols-12 gap-2 mt-4">
      <div class="col-span-8">
        <!-- Information -->
        <lazy-video-information hydrate-on-idle />

        <!-- Comments -->
        <suspense>
          <template #default>
            <client-only>
              <async-video-comment-section />
            </client-only>
          </template>

          <template #fallback>
            <u-skeleton class="w-full" />
          </template>
        </suspense>
      </div>

      <!-- Recommendations -->
      <div class="col-span-4">
        <u-card>
          Filters
        </u-card>

        <suspense>
          <template #default>
            <client-only>
              <async-recommendation-section />
            </client-only>
          </template>

          <template #fallback>
            <u-skeleton class="w-full" />
          </template>
        </suspense>
      </div>

      <!-- Modals -->
      <client-only>
        <lazy-modals-save hydrate-on-visible />
        <lazy-modals-report hydrate-on-visible />
        <lazy-modals-gift hydrate-on-visible />
        <lazy-modals-classification hydrate-on-visible />
        <lazy-modals-donation hydrate-on-visible />
        <lazy-modals-share hydrate-on-visible />
      </client-only>
    </section>
  </section>
</template>

<script setup lang="ts">
/**
 * Async Components
 */

const AsyncVideoCommentSection = defineAsyncComponent({
  loader: () => import('~/components/video/comment/Section.vue'),
  timeout: 5000
})

const AsyncRecommendationSection = defineAsyncComponent({
  loader: () => import('~/components/video/UserRecommendations.vue'),
  timeout: 5000
})

/**
 * Get Video
 */

const { id: videoId } = useRoute().params as { id: string }
const { data: currentVideo, status } = await useAsyncData(`video-${videoId}`, async () => await $fetch<VideoDetails>(`/api/videos/${videoId}`, {
  method: 'POST'
}), {
  lazy: true,
  default: () => ({} as VideoDetails)
})

const isLoading = computed(() => toValue(status) !== 'pending')

provide(IS_LOADING_SYMBOL, isLoading)
provide(CURRENT_VIDEO_SYMBOL, currentVideo)

/**
 * Video
 */

const videoSource = computed(() => currentVideo && isDefined(currentVideo) ? currentVideo.value.video : '')

/**
 * Playing Details & History
 */

const playingDetails = ref<VideoTechnicalDetails>()

function handleLoadedMetaData (data: VideoTechnicalDetails) {
  playingDetails.value = data
}

/**
 * Modals
 */

const { openModal } = useVideoDetailProvider()
</script>
