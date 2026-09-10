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

    <section id="information" class="mt-4">
      <!-- Actions -->
      <video-actions-card @action:modal="openModal" />

      <!-- Information -->
      <lazy-video-information hydrate-on-idle />
    </section>

    <section class="grid grid-cols-12 gap-2 mt-4">
      <!-- Comments -->
      <div class="col-span-8">
        <suspense>
          <template #default>
            <client-only>
              <async-video-comment-section />
            </client-only>
          </template>

          <template #fallback>
            <volt-skeleton height="100px" />
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
            <volt-skeleton height="100px" />
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

provideLocal(IS_LOADING_SYMBOL, ref<boolean>(true))
provideLocal(CURRENT_VIDEO_SYMBOL, ref<Undefineable<VideoDetails>>(undefined))

const isLoading = injectLocal<Ref<boolean>>(IS_LOADING_SYMBOL)
const currentVideo = injectLocal<Ref<Undefineable<VideoDetails>>>(CURRENT_VIDEO_SYMBOL)

try {
  const { id: videoId } = useRoute().params as { id: string }
  // const data = await $fetch<VideoDetails>(`/api/videos/${videoId}`, {
  //   method: 'POST'
  // })
  const { data } = await useAsyncData(`video-${videoId}`, () => $fetch<VideoDetails>(`/api/videos/${videoId}`, {
    method: 'POST'
  }), {
    default: () => ({} as VideoDetails)
  })
  
  if (isLoading) isLoading.value = false
  if (currentVideo) currentVideo.value = toValue(data)
} catch (e) {
  console.log(e)
}

/**
 * Video
 */

const videoSource = computed(() => currentVideo && isDefined(currentVideo) ? currentVideo.value.video : '')
// const videoSource = ref(undefined)

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
