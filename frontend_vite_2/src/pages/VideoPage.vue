<template>
  <section id="video">
    <section class="row">
      <div v-if="currentVideo" class="col-12">
        <!-- <base-video-player :video-source="mediaPath(currentVideo.video)" /> -->
        <base-video-player :video-source="`http://127.0.0.1:8000/api/v1/videos/s/${currentVideo.video_id}`" />
      </div>
    </section>

    <section class="row mt-4">
      <!-- Actions -->
      <BaseSkeleton :loading="isLoading">
        <user-video-actions @gifts="showGiftsModal = true" @report="showReportModal = true" @classify="showClassificationDrawer = true" @save="handleSave" />
      </BaseSkeleton>

      <!-- Information -->
      <BaseSkeleton :loading="isLoading">
        <video-information />
      </BaseSkeleton>
    </section>

    <section class="row mt-4">
      <!-- Comments -->
      <div class="col-8">
        <suspense>
          <template #default>
            <comment-section />
          </template>

          <template #fallback>
            <BaseSkeleton :loading="true" />
          </template>
        </suspense>
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
            <recommendation-section />
          </template>

          <template #fallback>
            <BaseSkeleton :loading="true" />
          </template>
        </suspense>
      </div>
    </section>

    <!-- Modals -->
    <teleport to="body">
      <v-navigation-drawer id="classification-modal" v-model="showClassificationDrawer" location="right" :width="400" temporary>
        <div class="container">
          <div class="row">
            <div class="col-12">
              <h2 class="h5">
                Classification
              </h2>

              <div class="alert alert-warning">
                Use this tool to signal that this video was not properly
                categorized by the creator and therefore does not correspond to
                the result you were expecting
              </div>

              <v-list>
                <v-list-item>
                  <v-switch label="Mark as wrong category" inset />
                </v-list-item>

                <v-list-item>
                  <v-switch label="Block this channel" inset />
                </v-list-item>
              </v-list>

              <v-divider />
            </div>
          </div>
        </div>

        <template #append>
          <div class="d-flex justify-content-end gap-2 mt-3 p-4">
            <v-btn variant="outlined" color="primary" rounded="xl" flat @click="showClassificationDrawer = false">
              Cancel
            </v-btn>

            <v-btn color="primary" rounded="xl" flat>
              <font-awesome-icon :icon="['fas', 'fa-save']" class="me-2" />
              Save
            </v-btn>
          </div>
        </template>
      </v-navigation-drawer>
    </teleport>

    <teleport to="body">
      <v-dialog id="report-video" v-model="showReportModal" width="400">
        <v-card>
          <v-card-text>
            <v-expansion-panels>
              <v-expansion-panel v-for="reportType in reportTypes" :key="reportType.title" :title="reportType.title" text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima" />
            </v-expansion-panels>

            <p class="fw-bold mt-5">
              Flag the section you believe to be problematic
            </p>

            <div class="d-flex justify-content-between gap-2">
              <v-text-field type="time" variant="outlined" />
              <v-text-field type="time" variant="outlined" />
            </div>

            <div class="alert alert-info">
              Flagged videos and users are reviewed by YouTube staff 24 hours a day,
              7 days a week to determine whether they violate Community Guidelines.
              Accounts are penalized for Community Guidelines violations, and
              serious or repeated violations can lead to account termination.
              Report channel
            </div>
          </v-card-text>

          <v-card-actions>
            <v-btn @click="showReportModal = false">
              Cancel
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </teleport>

    <teleport to="body">
      <v-dialog id="gifts" v-model="showGiftsModal" width="400" persistent>
        <v-card>
          <v-card-text>
            <div class="alert alert-danger">
              You have purchased no gifts yet. You can buy gifts here before pursuing.
            </div>

            <v-list>
              <v-list-item>
                <div class="d-flex justify-content-between">
                  <span>Google</span>
                  <v-btn>Faire un don</v-btn>
                </div>
              </v-list-item>
            </v-list>
          </v-card-text>

          <v-card-actions>
            <v-btn @click="showGiftsModal = false">
              Cancel
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </teleport>

    <teleport to="body">
      <v-dialog id="notes" width="400" persistent>
        <v-card>
          <v-card-text>
            Some text
          </v-card-text>
        </v-card>
      </v-dialog>
    </teleport>

    <teleport to="body">
      <v-dialog id="save" v-model="showSaveModal" width="400" persistent>
        <v-card>
          <v-card-text>
            <v-autocomplete v-model="selectedPlaylistId" :items="availablePlaylists" variant="solo-filled" item-title="name" item-value="playlist_id" clearable auto-select-first>
              <v-text-field placeholder="Select a playlist" />
            </v-autocomplete>
          </v-card-text>

          <v-card-actions>
            <v-btn @click="showSaveModal = false">
              Close
            </v-btn>

            <v-btn @click="requestSaveToPlaylist">
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </teleport>
  </section>
</template>

<script lang="ts">
import { defineAsyncComponent, defineComponent, provide, ref } from 'vue'
import { useFeed } from '../store/feed'
import { storeToRefs } from 'pinia'

import { Video } from '@/types/feed'

import reportTypes from '../data/report_types.json'

import BaseVideoPlayer from '@/components/BaseVideoPlayer.vue'
import BaseSkeleton from '@/components/BaseSkeleton.vue'
import UserVideoActions from '@/components/video/UserVideoActions.vue'
import VideoInformation from '@/components/video/VideoInformation.vue'

export default defineComponent({
  name: 'VideoPage',
  components: {
    BaseSkeleton,
    BaseVideoPlayer,
    UserVideoActions,
    VideoInformation,
    CommentSection: defineAsyncComponent({
      loader: () => import('@/components/video/AsyncCommentSection.vue'),
      delay: 600
    }),
    RecommendationSection: defineAsyncComponent({
      loader: () => import('@/components/video/UserRecommendations.vue')
    })
  },
  setup () {
    const isLoading = ref(true)
    const store = useFeed()
    const { currentVideo } = storeToRefs(store)

    const showClassificationDrawer = ref(false)
    const showReportModal = ref(false)
    const showGiftsModal = ref(false)
    const showSaveModal = ref(false)

    const availablePlaylists = ref([])

    const selectedPlaylistId = ref(null)
    provide('currentVideo', currentVideo)

    return {
      isLoading,
      selectedPlaylistId,
      availablePlaylists,
      currentVideo,
      reportTypes,
      showGiftsModal,
      showSaveModal,
      showClassificationDrawer,
      showReportModal
    }
  },
  mounted () {
    this.requestVideoDetails()
  },
  methods: {
    /**
     * 
     */
    async requestVideoDetails () {
      try {
        const videoID = this.$route.params.id
        const response = await this.$client.get<Video>(`/videos/${videoID}`)
        this.currentVideo = response.data
        this.isLoading = false
      } catch (e) {
        console.log(e)
      }
    },
    /**
     * 
     */
    async requestSaveToPlaylist () {
      try {
        await this.$client.post(`/playlists/${this.selectedPlaylistId}/add`, {
          video: this.$route.params.id
        })
      } catch (e) {
        console.error('requestSaveToPlaylist', e)
      }
    },
    /**
     * 
     */
    handleSave (playlists) {
      this.showSaveModal = true
      this.availablePlaylists = playlists
    },
    /**
     * 
     */
    mediaPath (path: string) {
      if (path) {
        const instance = new URL(path, import.meta.env.VITE_ROOT_DEVELOPMENT_URL)
        return instance.toString()
      } else {
        return ''
      }
    }
  }
})
</script>
