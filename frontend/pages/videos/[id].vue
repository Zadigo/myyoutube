<template>
  <section id="video">
    <section class="row">
      <div v-if="currentVideo" class="col-12">
        <!-- <BaseVideoPlayer :video-source="videoSource" /> -->
      </div>
    </section>

    <div class="container">
      <section class="row mt-4">
        <!-- Actions -->
        <BaseSkeleton :loading="isLoading">
          <VideoUserActions @action="handleAction" @update-playlists="handleSaveToPlaylist" />
        </BaseSkeleton>

        <!-- Information -->
        <BaseSkeleton :loading="isLoading">
          <VideoInformation />
        </BaseSkeleton>
      </section>

      <section class="row mt-4">
        <!-- Comments -->
        <div class="col-8">
          <Suspense>
            <template #default>
              <AsyncVideoCommentSection />
            </template>

            <template #fallback>
              <BaseSkeleton :loading="true" />
            </template>
          </Suspense>
        </div>

        <!-- Recommendations -->
        <div class="col-4">
          <div class="card">
            <div class="card-body">
              Filters
            </div>
          </div>

          <suspense>
            <template #default>
              <AsyncRecommendationSection />
            </template>

            <template #fallback>
              <BaseSkeleton :loading="true" />
            </template>
          </suspense>
        </div>
      </section>
    </div>

    <!-- Modals -->
    <ClientOnly>
      <ModalsClassification v-model="showClassificationDrawer" />
      <ModalsReport v-model="showReportModal" />
      <ModalsGift v-model="showGiftsModal" />
      <!-- TODO: Remove in favor the fact checking center -->
      <ModalsCommunityNotes v-model="showCommunityNotes" />
      <ModalsSave v-model="showSaveModal" :playlists="availablePlaylists" />
      <ModalsDonation v-model="showDonationModal" />
      <ModalsShare v-model="showShareModal" />
    </ClientOnly>
  </section>
</template>

<script setup lang="ts">
import type { Playlist, VideoInfo, VideoMenuAction } from '~/types'

const AsyncVideoCommentSection = defineAsyncComponent({
  loader: () => import('~/components/video/AsyncCommentSection.vue'),
  timeout: 5000
})

const AsyncRecommendationSection = defineAsyncComponent({
  loader: () => import('~/components/video/UserRecommendations.vue'),
  timeout: 5000
})

const store = useFeed()
const { $client } = useNuxtApp()
const route = useRoute()
const { currentVideo } = storeToRefs(store)

const availablePlaylists = ref<Playlist[]>([])
const isLoading = ref(true)
const showClassificationDrawer = ref(false)
const showReportModal = ref(false)
const showGiftsModal = ref(false)
const showSaveModal = ref(false)
const showShareModal = ref(false) 
const showDonationModal = ref(false)
const showCommunityNotes = ref(false)

provide('currentVideo', currentVideo)

const videoSource = computed(() => {
  if (currentVideo.value) {
    // return `http://127.0.0.1:8000/api/v1/videos/s/${currentVideo.value.video_id}`
    return getBaseUrl(`/api/v1/videos/s/${currentVideo.value.video_id}`)
  } else {
    return ''
  }
})

async function requestVideoDetails () {
  try {
    const videoID = route.params.id
    const response = await $client.get<VideoInfo>(`/videos/${videoID}`)
    
    currentVideo.value = response.data
    isLoading.value = false
  } catch (e) {
    console.log(e)
  }
}

function handleAction (action: VideoMenuAction) {
  if (action === 'Gift') {
    showGiftsModal.value = true
  }

  if (action === 'Save') {
    showSaveModal.value = true
  }

  if (action === 'Store') {
    // Pass
  }

  if (action === 'Recommendations') {
    showClassificationDrawer.value = true
  }

  if (action === 'Donate') {
    showDonationModal.value = true
  }

  if (action === 'Report') {
    showReportModal.value = true
  }

  if (action === 'Share') {
    showShareModal.value = true
  }

  if (action === 'Classify') {
    showClassificationDrawer.value = true
  }
}

function handleSaveToPlaylist (playlists: Playlist[]) {
  showSaveModal.value = true
  availablePlaylists.value = playlists
}

onMounted(async () => {
  await requestVideoDetails()
  // await requestPlaylists()
})
</script>
