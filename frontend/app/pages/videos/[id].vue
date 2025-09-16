<template>
  <section id="video-details">
    <ClientOnly>
      <section v-if="currentVideo" id="video-player">
        <VideoPlayerBase :video-source="videoSource" @update:details="handleLoadedMetaData" />
      </section>
    </ClientOnly>

    <section id="information" class="mt-4">
      <!-- Actions -->
      <VideoActionsCard @action="openModal" />

      <!-- Information -->
      <VideoInformation />
    </section>

    <section class="grid grid-cols-12 gap-2 mt-4">
      <!-- Comments -->
      <div class="col-span-8">
        <Suspense>
          <template #default>
            <ClientOnly>
              <AsyncVideoCommentSection />
            </ClientOnly>
          </template>

          <template #fallback>
            <VoltSkeleton height="100px" />
          </template>
        </Suspense>
      </div>

      <!-- Recommendations -->
      <div class="col-span-4">
        <VoltCard>
          <template #content>
            Filters
          </template>
        </VoltCard>

        <Suspense>
          <template #default>
            <ClientOnly>
              <AsyncRecommendationSection />
            </ClientOnly>
          </template>

          <template #fallback>
            <VoltSkeleton height="100px" />
          </template>
        </Suspense>
      </div>
    </section>

    <!-- Modals -->
    <ClientOnly>
      <ModalsSave v-model="showSaveModal" />
      <ModalsReport v-model="showReportModal" />
      <ModalsGift v-model="showGiftsModal" />
      <ModalsClassification v-model="showClassificationDrawer" />
      
      <!-- 
      -->
      <!-- TODO: Remove in favor the fact checking center -->
      <!-- <ModalsCommunityNotes v-model="showCommunityNotes" />
      <ModalsDonation v-model="showDonationModal" />
      <ModalsShare v-model="showShareModal" /> -->
    </ClientOnly>
  </section>
</template>

<script setup lang="ts">
import { useVideoDetailModals } from '~/composables/use'

import type { VideoTechnicalDetails } from '~/types'

const AsyncVideoCommentSection = defineAsyncComponent({
  loader: () => import('~/components/video/comment/Section.vue'),
  timeout: 5000
})

const AsyncRecommendationSection = defineAsyncComponent({
  loader: () => import('~/components/video/UserRecommendations.vue'),
  timeout: 5000
})

const videoDetailStore = useVideoDetailStore()
const { currentVideo, isLoading } = storeToRefs(videoDetailStore)

provide('currentVideo', currentVideo)
provide('isLoading', isLoading)

videoDetailStore.getVideo()

const { showClassificationDrawer, showReportModal, showGiftsModal, showSaveModal, showShareModal, showDonationModal, showCommunityNotes, openModal  } = useVideoDetailModals()

const videoSource = computed(() => '/video_fixture_1.mp4')

/**
 * Video
 */

const playingDetails = ref<VideoTechnicalDetails>()
const { history } = useRefHistory(playingDetails)

console.log(history)

function handleLoadedMetaData (data: VideoTechnicalDetails) {
  playingDetails.value = data
}
</script>
