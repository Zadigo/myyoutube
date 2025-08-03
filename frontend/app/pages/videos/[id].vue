<template>
  <section id="video-details">
    <section v-if="currentVideo" id="video-player">
      <!-- <VideoPlayerBase :video-source="videoSource" /> -->
      <!-- <BaseVideoPlayer :video-source="videoSource" /> -->
    </section>

    <section id="information" class="mt-4">
      <!-- Actions -->
      <!-- @action="openModal" -->
      <VideoActionsCard />

      <!-- Information -->
      <VideoInformation />
    </section>

    <section class="grid grid-cols-12 mt-4">
      <!-- Comments -->
      <div class="col-span-8">
        <!-- <Suspense>
          <template #default>
            <AsyncVideoCommentSection />
          </template>

          <template #fallback>
            <BaseSkeleton :loading="true" />
          </template>
        </Suspense> -->
      </div>

      <!-- Recommendations -->
      <div class="col-span-4">
        <VoltCard class="card">
          <template #content>
            Filters
          </template>
        </VoltCard>

        <!-- <suspense>
          <template #default>
            <AsyncRecommendationSection />
          </template>

          <template #fallback>
            <BaseSkeleton :loading="true" />
          </template>
        </suspense> -->
      </div>
    </section>

    <!-- Modals -->
    <ClientOnly>
      <!-- <ModalsClassification v-model="showClassificationDrawer" />
      <ModalsReport v-model="showReportModal" />
      <ModalsGift v-model="showGiftsModal" /> -->
      <!-- TODO: Remove in favor the fact checking center -->
      <!-- <ModalsCommunityNotes v-model="showCommunityNotes" />
      <ModalsSave v-model="showSaveModal" />
      <ModalsDonation v-model="showDonationModal" />
      <ModalsShare v-model="showShareModal" /> -->
    </ClientOnly>
  </section>
</template>

<script setup lang="ts">
import { useVideoDetailModals } from '~/composables/use'

// const AsyncVideoCommentSection = defineAsyncComponent({
//   loader: () => import('~/components/video/AsyncCommentSection.vue'),
//   timeout: 5000
// })

// const AsyncRecommendationSection = defineAsyncComponent({
//   loader: () => import('~/components/video/UserRecommendations.vue'),
//   timeout: 5000
// })

const videoDetailStore = useVideoDetailStore()
const { currentVideo, isLoading } = storeToRefs(videoDetailStore)

provide('currentVideo', currentVideo)
provide('isLoading', isLoading)

console.log('[id]', currentVideo)

videoDetailStore.testRun()

const { showClassificationDrawer, showReportModal, showGiftsModal, showSaveModal, showShareModal, showDonationModal, showCommunityNotes, openModal  } = useVideoDetailModals()

const videoSource = computed(() => '/video_fixture_1.mp4')
</script>
