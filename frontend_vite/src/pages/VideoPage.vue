<template>
  <section id="video">
    <section class="row">
      <div class="col-12">
        <base-video-player :video-source="mediaPath(currentVideo.video)" />
      </div>
    </section>

    <section class="row mt-4">
      <!-- Actions -->
      <user-video-actions @gifts="showGiftsModal = true" @report="showReportModal = true" @classify="showClassificationDrawer = true" />

      <!-- Information -->
      <video-information />
    </section>

    <section class="row mt-4">
      <div class="col-8">
        <div class="card">
          <div class="card-body">
            <div class="d-flex align-items-center justify-content-between">
              <h2 class="h4 m-0">6,909 Comments</h2>

              <v-menu>
                <template #activator="{ props }">
                  <v-btn v-bind="props" rounded="xl" color="primary" flat>
                    <font-awesome-icon :icon="['fas', 'fa-sort']" class="me-3" />
                    Sort
                  </v-btn>
                </template>

                <v-list>
                  <v-list-item v-for="sortAction in sortActions" :key="sortAction">
                    <v-list-item-title>{{ sortAction }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </div>
          </div>

          <hr class="text-body-tertiary">

          <!-- Comment Actions -->
          <user-comment-actions @new-comment="handleNewComment" />

          <!-- Comments -->
          <transition-group id="comments" tag="div">
            <user-comment v-for="comment in comments" :key="comment.id" :comment="comment" />
          </transition-group>
        </div>
      </div>

      <!-- Recommendations -->
      <div class="col-4">
        <div class="card">
          <div class="card-body"></div>
        </div>

        <suspense>
          <template #default>
            <recommendation-section />
          </template>
        </suspense>
      </div>
    </section>

    <!-- Modals -->
    <v-navigation-drawer id="classification-modal" v-model="showClassificationDrawer" location="right" :width="400" temporary>
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="h5">Classification</h2>

            <div class="alert alert-warning">
              Use this tool to signal that this video was not properly
              categorized by the creator and therefore does not correspond to
              the result you were expecting
            </div>

            <v-list>
              <v-list-item>
                <v-switch label="Mark as wrong category" inset></v-switch>
              </v-list-item>

              <v-list-item>
                <v-switch label="Block this channel" inset></v-switch>
              </v-list-item>
            </v-list>

            <v-divider></v-divider>
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

    <v-dialog id="report-video" v-model="showReportModal" width="400">
      <v-card>
        <v-card-text>

          <v-expansion-panels>
            <v-expansion-panel v-for="reportType in reportTypes" :key="reportType.title" :title="reportType.title" text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima"></v-expansion-panel>
          </v-expansion-panels>

          <p class="fw-bold mt-5">Flag the section you believe to be problematic</p>
          <div class="d-flex justify-content-between gap-2">
            <v-text-field type="time" variant="outlined"></v-text-field>
            <v-text-field type="time" variant="outlined"></v-text-field>
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
          <v-btn @click="showReportModal = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

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
          <v-btn @click="showGiftsModal = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog id="notes" width="400" persistent>
      <v-card>
        <v-card-text>

        </v-card-text>
      </v-card>
    </v-dialog>
  </section>
</template>

<script>
import { defineAsyncComponent, provide, ref } from 'vue'
import { useFeed } from '../store/feed'
import { storeToRefs } from 'pinia'

import reportTypes from '../data/report_types.json'

import BaseVideoPlayer from '../components/BaseVideoPlayer.vue'
import UserComment from '../components/video/UserComment.vue'
import UserVideoActions from '../components/video/UserVideoActions.vue'
import UserCommentActions from '../components/video/UserCommentActions.vue'
import VideoInformation from 'src/components/video/VideoInformation.vue'

const sortActions = [
  'Newest',
  'Oldest'
]

export default {
  name: 'VideoPage',
  components: {
    BaseVideoPlayer,
    UserComment,
    UserCommentActions,
    UserVideoActions,
    VideoInformation,
    RecommendationSection: defineAsyncComponent({
      loader: () => import('src/components/video/UserRecommendations.vue')
    })
  },
  setup () {
    const store = useFeed()
    const { currentVideo } = storeToRefs(store)

    const showClassificationDrawer = ref(false)
    const showReportModal = ref(false)
    const showGiftsModal = ref(false)
    const comments = ref([{}, {}, {}])

    provide('currentVideo', currentVideo)

    return {
      currentVideo,
      comments,
      reportTypes,
      showGiftsModal,
      showClassificationDrawer,
      showReportModal,
      sortActions
    }
  },
  mounted () {
    this.requestVideoDetails()
  },
  methods: {
    async requestVideoDetails () {
      // Get all the details to display the
      // video correctly to the user
      try {
        const videoID = this.$route.params.id
        const response = await this.$client.post(`/videos/detail/${videoID}`)
        this.currentVideo = response.data

        setTimeout(() => {
          this.requestVideoComments()
        }, 2000)
      } catch (e) {
        console.log(e)
      }
    },
    async requestVideoComments () {
      // Get all the comments for the current video
      // in a delayed manner for performance optimization
      try {
        const videoID = this.$route.params.id
        const response = await this.$client.get(`/comments/${videoID}`)
        this.comments = response.data
      } catch (e) {
        console.log(e)
      }
    },
    handleNewComment (comment) {
      // Append the newly created comment at the
      // start of the current comment list
      this.comments.unshift(comment)
    },
    mediaPath (path) {
      if (path) {
        const instance = new URL(path, import.meta.env.VITE_ROOT_DEVELOPMENT_URL)
        console.log(instance.toString())
        return instance.toString()
      } else {
        return ''
      }
    }
  }
}
</script>
