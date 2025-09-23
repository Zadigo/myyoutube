<template>
  <section id="video-details">
    <client-only>
      <section v-if="currentVideo" id="video-player">
        <video-player-base :video-source="videoSource" @update:details="handleLoadedMetaData" />
      </section>
    </client-only>

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

    <!-- Modals -->
    <client-only>
      <modals-save v-model="showSaveModal" />
      <modals-report v-model="showReportModal" />
      <modals-gift v-model="showGiftsModal" />
      <modals-classification v-model="showClassificationDrawer" />

      <!--
      -->
      <!-- TODO: Remove in favor the fact checking center -->
      <!-- <ModalsCommunityNotes v-model="showCommunityNotes" />
      <ModalsDonation v-model="showDonationModal" />
      <ModalsShare v-model="showShareModal" /> -->
    </client-only>
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
