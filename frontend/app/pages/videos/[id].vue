<template>
  <section id="video-details">
    <!-- Video -->
    <section id="video-player">
      <client-only>
        <video-player-base :video-source="videoSource" @update:details="handleLoadedMetaData" />
      </client-only>
    </section>

    <section id="information" class="mt-4">
      <!-- Actions -->
      <video-actions-card @action="openModal" />

      <!-- Information -->
      <video-information />
    </section>

    <section class="grid grid-cols-12 gap-2 mt-4">
      <!-- Comments -->
      <div class="col-span-8">
        <Suspense>
          <template #default>
            <client-only>
              <async-video-comment-section />
            </client-only>
          </template>

          <template #fallback>
            <volt-skeleton height="100px" />
          </template>
        </Suspense>
      </div>

      <!-- Recommendations -->
      <div class="col-span-4">
        <volt-card>
          <template #content>
            Filters
          </template>
        </volt-card>

        <Suspense>
          <template #default>
            <client-only>
              <async-recommendation-section />
            </client-only>
          </template>

          <template #fallback>
            <volt-skeleton height="100px" />
          </template>
        </Suspense>
      </div>
    </section>
  </section>
</template>

<script setup lang="ts">
// import { useVideoDetailModals } from '~/composables/use'
import { currentVideoSymbol, isLoadingSymbol } from '~/data/constants'
import type { BaseVideo, Undefineable, VideoTechnicalDetails } from '~/types'

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

provideLocal(isLoadingSymbol, ref<boolean>(true))
provideLocal(currentVideoSymbol, ref<Undefineable<BaseVideo>>(undefined))

const isLoading = injectLocal<Ref<boolean>>(isLoadingSymbol)
const currentVideo = injectLocal<Ref<Undefineable<BaseVideo>>>(currentVideoSymbol)

try {
  const { id: videoId } = useRoute().params as { id: string }
  const data = await $fetch<BaseVideo>(`/api/videos/${videoId}`, { method: 'GET' })

  isLoading.value = false
  currentVideo.value = data
} catch (e) {
  console.log(e)
}

/**
 * Modals
 */

const { showClassificationDrawer, showReportModal, showGiftsModal, showSaveModal, showShareModal, showDonationModal, showCommunityNotes, openModal  } = useVideoDetailModals()

/**
 * Video
 */

const videoSource = computed(() => isDefined(currentVideo) ? currentVideo.value.video : '')
// const videoSource = ref(undefined)

const playingDetails = ref<VideoTechnicalDetails>()
const { history } = useRefHistory(playingDetails)

console.log(history)

function handleLoadedMetaData (data: VideoTechnicalDetails) {
  playingDetails.value = data
}
</script>
