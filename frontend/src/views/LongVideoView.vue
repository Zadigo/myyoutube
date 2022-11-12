<template>
  <base-site-vue>
    <section id="youtube">
      <div class="container-fluid p-0">
        <!-- Player -->
        <base-video-wrapper>
          <template #default>
            <base-video-player-vue :video-url="require('@/assets/video2_full_hd.mp4')" />
          </template>
        </base-video-wrapper>
        

        <div class="position-relative">
          <!-- Information -->
          <div class="row">
            <div class="col-12">
              <!-- Warning Banner -->
              
              <!-- Video Infos -->
              <div class="card mt-2">
                <div class="card-body">
                  <h5 class="card-title w-100">
                    {{ currentVideo.title }}
                  </h5>

                  <div :class="{ 'flex-column': breakpoints.isSmaller('md') }" class="d-flex justify-content-between">
                    <span :class="{ 'mb-2': breakpoints.isSmaller('md') }" class="text-muted">
                      {{ currentVideo.views }} views - {{ currentVideo.created_on }}
                    </span>

                    <!-- Actions -->
                    <div class="d-flex justify-content-around">
                      <div class="btn-group shadow-none btn-rounded">
                        <button type="button" class="btn btn-lg btn-primary" @click="likeVideo">
                          <font-awesome-icon icon="fa-solid fa-thumbs-up" class="me-2" />
                          {{ currentVideo.likes }}
                        </button>

                        <button type="button" class="btn btn-lg btn-primary" @click="likeVideo">
                          <font-awesome-icon icon="fa-solid fa-thumbs-down" class="me-2" />
                          {{ currentVideo.dislikes }}
                        </button>
                      </div>

                      <!-- More -->
                      <base-dropdown-button-vue :items="moreButtonOptions" button-name="More" color="secondary" size="lg" class="mx-2 shadow-none" @dropdown-click="dropdownClick" />

                      <div class="btn-group shadow-none">
                        <button type="button" class="btn btn-primary btn-lg" @click="currentVideo.channel.subscribed = !currentVideo.channel.subscribed">
                          <span v-if="currentVideo.channel.subscribed">{{ $t('Unsubscribe') }}</span>
                          <span v-else>{{ $t('Subscribe') }}</span>
                        </button>

                        <button v-if="currentVideo.channel.subscribed" type="button" class="btn btn-primary btn-lg" @click="currentVideo.channel.notifications = !currentVideo.channel.notifications">
                          <font-awesome-icon v-if="currentVideo.channel.notifications" icon="fa-solid fa-bell-slash" />
                          <font-awesome-icon v-else icon="fa-solid fa-bell" />
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- Account Infos -->
              <div class="card my-2">
                <div class="card-body">
                  <div class="row">
                    <div class="col-2">
                      <router-link :to="{ name: 'channel_view'}">
                        <img :src="require('@/assets/avatar3.png')" class="img-fluid rounded-circle" alt="Image 6">
                      </router-link>
                    </div>

                    <div class="col-10">
                      <router-link :to="{ name: 'channel_view' }" class="fw-bold mb-0">
                        {{ currentVideo.channel.name }}
                        <font-awesome-icon v-if="currentVideo.channel.verified" icon="fa-solid fa-circle-check" class="text-primary mx-1" />
                      </router-link>

                      <p class="text-muted fw-light m-0">{{ formatSubscribers(currentVideo.channel.subscribers) }} subscribers</p>

                      <!-- Categories -->
                      <base-scrollbar-vue :items="currentVideo.categories" class="my-3" />

                      <div class="alert alert-info w-50">
                        Music video/Video clip : <span class="fw-bold">UMG/Digital Universal</span>
                        <button type="button" class="btn btn-rounded mt-3">Discography</button>
                      </div>

                      <p id=" description">
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                        Sequi porro iure repellat optio, ipsum ducimus veniam natus ipsam dolor,
                        suscipit distinctio vero? Labore repellendus ipsum et cumque fuga?
                        Ullam, nam!

                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates id pariatur
                        fuga molestiae aperiam inventore repellendus, dolorum ducimus saepe fugiat minima
                        quisquam. Deleniti, ratione? Quis et harum ullam ab nam.
                      </p>

                      <button type="button" class="btn btn-light shadow-none">Show more</button>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Albums or songs -->
              <!-- <div class="card my-2">
                <div class="card-body">
                  <div class="d-flex justify-content-left gap-2">
                    <div v-for="i in 5" :key="i" class="card">
                      <img :src="require('@/assets/cover.jpg')" class="card-img-top" alt="">
                      <router-link :to="{ name: 'home_view'}" class="text-dark">
                        <div class="card-body">
                          <h6 class="card-title">Lanae Good Good!</h6>
                          <p class="text-muted m-0">1998</p>
                        </div>
                      </router-link>
                    </div>
                  </div>
                </div>
              </div> -->

              <!-- Donation - Cause -->
            </div>
          </div>

          <div class="row">
            <!-- Comments -->
            <comment-section :current-video="currentVideo" :shadow="false" />

            <!-- Playlists -->
            <!-- <div class="col-sm-12 col-md-4">
              <div class="card">
                <div v-if="inPlaylist" class="card-body">
  
                </div>
              </div>
            </div> -->

            <!-- Recommendations -->
            <div v-if="breakpoints.isGreater('sm')" class="col-sm-12 col-md-4">

              <div class="card mb-3">
                <div class="card-body">
                  <div class="d-flex justify-content-between">
                    <button type="button" class="btn btn-sm btn-secondary btn-rounded shadow-none" @click="updateRecommendations">
                      <font-awesome-icon icon="fa-solid fa-refresh" class="me-2" />
                      {{ $t('Load more') }}
                    </button>

                    <router-link :to="{ name: 'home_view' }" class="btn btn-sm btn-secondary btn-rounded shadow-none">
                      <font-awesome-icon icon="fa-solid fa-expand" class="me-2" />
                      {{ $t('See all') }}
                    </router-link>
                  </div>
                </div>
              </div>

              <div v-if="isLoadingRecommendations" class="text-center my-4">
                <div class="spinner-border" role="status">
                  <span class="visually-hidden">Loading...</span>
                </div>
              </div>

              <list-recommendations-vue v-else :recommendations="recommendations" />
            </div>

            <!-- Mobile Recommendations -->
            <recommendation-drawer-vue v-else :show="showRecommendationsDrawer" :recommendations="recommendations" />
          </div>
        </div>
      </div>

      <!-- Modals -->
      <base-modal-vue id="donation" :show="showDonationModal" :title="$t('Make a donation')" @close="showDonationModal = false">
        <div class="row">
          <div class="col-12">
            <div class="alert alert-info">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque minima
              ipsam placeat est ex? Doloremque, nemo architecto provident necessitatibus
              sequi modi dolorem! Ab rem inventore esse libero laudantium animi dicta!
            </div>

            <div class="col-12">
              <input type="range" min="0" max="50" step="5" class="form-range">

              <div class="form-check form-switch my-2">
                <input id="super-donation" class="form-check-input" type="checkbox" role="switch" />
                <label class="form-check-label" for="super-donation">
                  {{ $t('Make a super donation') }}
                </label>
              </div>

              <div class="alert alert-warning">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque minima
                ipsam placeat est ex? Doloremque, nemo architecto provident necessitatibus
                sequi modi dolorem! Ab rem inventore esse libero laudantium animi dicta!
              </div>

              <div class="alert alert-danger mt-2">
                You have no payment system on your account. Add a card to
                your account before doing so
              </div>

              <div class="form-check form-switch my-2">
                <input id="acceptance-text" class="form-check-input" type="checkbox" role="switch" />
                <label class="form-check-label" for="acceptance-text">
                  I consent to x an y and agree to donate $15 to this channel
                </label>
              </div>
            </div>
          </div>
        </div>

        <template #footer>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary">
              {{ $t('Send') }} - {{ $n(15, 'currency', $i18n.locale) }}
            </button>
          </div>
        </template>
      </base-modal-vue>

      <base-modal-vue id="store" :show="showStore" :scrollable="true" size="fullscreen" @close="showStore = false">
        <template #default>
          <div class="row">
            <div class="col-12">
              <div class="row mb-3">
                <div class="col-12">
                  <div class="alert alert-info my-2">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Amet sapiente fugiat incidunt quae quis sint necessitatibus sunt inventore
                    nisi blanditiis quod optio eos, obcaecati totam ullam. Nemo, officiis obcaecati.
                    Magnam!
                  </div>

                  <input type="search" class="form-control p-2" placeholder="Search products">
                </div>
              </div>

              <div class="row">
                <div v-for="i in 10" :key="i" class="col-2 mb-2">
                  <div class="card shadow-none">
                    <img src="https://via.placeholder.com/500" class="card-img-top" alt="Image 8">
                    <div class="card-body p-1 bg-transparent">
                      <h6 class="card-title">Some product</h6>
                      <button type="button" class="btn btn-primary btn-sm">
                        <font-awesome-icon icon="fa-solid fa-shopping-bag" class="me-2" />
                        {{ $t('Add to cart') }}
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </template>

        <template #footer>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary">
              Purchase <span class="badge text-bg-secondary">5</span> items
            </button>
          </div>
        </template>
      </base-modal-vue>

      <base-modal-vue id="gift" :show="showGifts" :scrollable="true" size="sm" @close="showGifts = false">
        <div class="row">
          <div class="col-12">
            <div class="alert alert-danger">
              You have purchased no gifts yet. You can buy
              gifts here before pursuing.
            </div>

            <div class="list-group">
              <a v-for="i in 5" :key="i" href class="list-group-item d-flex justify-content-between" @click.prevent>
                <span>Gift {{ i }}</span>
                <div class="btn-group shadow-none">
                  <button type="button" class="btn btn-sm btn-primary">
                    <font-awesome-icon icon="fa-solid fa-circle-dollar-to-slot" class="me-2" />
                    {{ $t('Donate') }}
                  </button>
                </div>
              </a>
            </div>
          </div>
        </div>
      </base-modal-vue>

      <base-modal-vue id="report" :show="showReport" :scrollable="true" :title="$t('Report video')" size="sm" @close="showReport = false">
        <div class="row">
          <div class="col-12">
            <base-accordion-vue :items="reports" />
          </div>

          <div class="col-12 my-4">
            <p class="mb-1">Flag the section you believe to be problematic</p>
            <div class="d-flex justify-content-between">
              <input type="time" class="form-control p-2">
              <input type="time" class="form-control p-2 ms-2">
            </div>
          </div>

          <div class="col-12">
            <p class="fw-light m-0 alert alert-info">
              Flagged videos and users are reviewed by YouTube staff 24 hours a day, 7 days a week to determine whether
              they violate Community Guidelines. Accounts are penalized for Community Guidelines violations, and serious
              or repeated violations can lead to account termination. Report channel
            </p>
          </div>
        </div>

        <template #footer>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary">
              {{ $t('Send') }}
            </button>
          </div>
        </template>
      </base-modal-vue>

      <base-offcanvas-vue id="playlists" :show="showPlaylists" title="Playlists" position="end" @close="showPlaylists = false">
        <base-list-group-checkbox id="playlists-group" :items="[{ name: 'Google' }]" />

        <button type="button" class="btn btn-md btn-primary mt-2" @click="showPlaylistCreationInput = true">
          <font-awesome-icon icon="fa-solid fa-plus" class="me-2" />
          {{ $t('Create') }}
        </button>
      </base-offcanvas-vue>

      <base-offcanvas-vue id="recommendation" :show="showRecommendationReport" title="Recommendation" position="end" @close="showRecommendationReport = false">
        <div class="row">
          <div class="col-12">
            <div class="alert alert-warning">
              Use this tool to signal that this video was not properly categorized
              by the creator and therefore does not correspond to the result you
              were expecting
            </div>

            <div class="list-group my-3">
              <div class="list-group-item">
                <div class="form-check form-switch">
                  <input id="wrong-category-alert" class="form-check-input" type="checkbox" role="switch" />
                  <label class="form-check-label" for="wrong-category-alert">
                    Mark as wrong category
                  </label>
                </div>
              </div>
            </div>

            <!-- <select class="form-select" aria-label="Expected category">
              <option selected>Expected category</option>
              <option value="1">One</option>
              <option value="2">Two</option>
              <option value="3">Three</option>
            </select> -->

            <base-select :items="['One', 'Two']" />

            <div class="list-group mt-3">
              <div class="list-group-item">
                <div class="form-check form-switch">
                  <input id="block-channel" class="form-check-input" type="checkbox" role="switch" />
                  <label class="form-check-label" for="block-channel">
                    {{ $t('Block this channel') }}
                  </label>
                </div>
              </div>
            </div>
          </div>
        </div>

        <template #footer>
          <div class="offcanvas-footer">
            <button type="button" class="btn btn-outline-danger" @click="showRecommendationReport = false">
              {{ $t('Close') }}
            </button>

            <button type="button" class="btn btn-primary ms-2">
              {{ $t('Save') }}
            </button>
          </div>
        </template>
      </base-offcanvas-vue>
    </section>
  </base-site-vue>
</template>

<script>
import video from '@/data/video'
import reports from '@/data/reports'
import useFormatting from '@/composables/formatting'

import { ref, provide } from 'vue'
import { breakpointsTailwind, useBreakpoints } from '@vueuse/core'

// import BaseDropGroupVue from '@/layouts/BaseDropGroup.vue'

import BaseVideoPlayerVue from '@/layouts/BaseVideoPlayer.vue'
import BaseListGroupCheckbox from '@/layouts/bootstrap/listgroups/BaseListGroupCheckbox.vue'
import BaseScrollbarVue from '@/layouts/BaseScrollbar.vue'
import BaseDropdownButtonVue from '@/layouts/bootstrap/BaseDropdownButton.vue'
import BaseModalVue from '@/layouts/BaseModal.vue'
import BaseOffcanvasVue from '@/layouts/bootstrap/BaseOffcanvas.vue'
import BaseAccordionVue from '@/layouts/BaseAccordion.vue'
import BaseSiteVue from '@/layouts/BaseSite.vue'
import BaseSelect from '@/layouts/bootstrap/BaseSelect.vue'
import CommentSection from '@/components/CommentSection.vue'
import ListRecommendationsVue from '@/components/youtube/ListRecommendations.vue'
import RecommendationDrawerVue from '@/components/youtube/RecommendationDrawer.vue'
import BaseVideoWrapper from '@/layouts/BaseVideoWrapper.vue'

export default {
  name: 'LongVideoView',
  components: {
    BaseVideoPlayerVue,
    BaseDropdownButtonVue,
    BaseModalVue,
    BaseAccordionVue,
    BaseListGroupCheckbox,
    // BaseDropGroupVue,
    BaseOffcanvasVue,
    BaseScrollbarVue,
    BaseSiteVue,
    BaseSelect,
    CommentSection,
    ListRecommendationsVue,
    RecommendationDrawerVue,
    BaseVideoWrapper
},
  setup () {
    const isLoading = ref(true)
    const breakpoints = useBreakpoints(breakpointsTailwind)
    provide('isLoading', isLoading)

    const { formatSubscribers } = useFormatting()

    return {
      formatSubscribers,
      breakpoints,
      reports
    }
  },
  data: () => ({
    isLoadingRecommendations: true,

    showDonationModal: false,
    showPlaylists: false,
    showStore: false,
    showGifts: false,
    showReport: false,
    showRecommendationReport: false,
    showRecommendationsDrawer: false,
    showPlaylistCreationInput: false,
    inPlaylist: false,

    sortMethod: 'Newest',

    currentVideo: video,

    lowerLimit: 0,
    upperLimit: 20,
    totalLimit: 20,
    recommendationLimit: 5,
    cachedRecommendations: [],

    moreButtonOptions: [
      { name: 'Store', icon: 'store' }, 
      { name: 'Download', icon: 'download' },
      { name: 'Save', icon: 'floppy-disk' }, 
      { name: 'Gift', icon: 'gift' }, 
      { name: 'Donate', icon: 'money-bill' }, 
      { name: 'Share', icon: 'share' }, 
      { name: 'Recommendation', icon: 'star' },
      { divider: true },
      { name: 'Report', icon: 'triangle-exclamation' }
    ],

    // Channel
    expandCard: false
  }),
  computed: {
    recommendations () {
      // We load a set of recommendations e.g. a 100 
      // that we will then slice to the user. This
      // prevents from making constant API calls to
      // the backend
      return this.cachedRecommendations.slice(this.lowerLimit, this.upperLimit)
    }
  },
  watch: {
    '$route.query.video' (current, previous) {
      if (current !== previous) {
        this.getVideo()
      }
    }
  },
  created () {
    // http://localhost:8080/video?playlist=true
    const inPlaylist = this.$route.query.playlist * 1
    const result = inPlaylist === 0 || inPlaylist === 1 ? inPlaylist : 0
    this.inPlaylist = result === 1
  },
  beforeMount () {
    this.getVideo()
    // TODO: totalLimit does not get set - we need to determine
    // how much groups of videos we need e.g. 100/5 = 20 per group
    this.totalLimit = 20
    // this.totalLimit = this.cachedRecommendations.length / this.recommendationLimit
    // this.upperLimit = this.totalLimit
  },
  mounted () {
    this.isLoadingRecommendations = false
  },
  methods: {
    getVideo () {
      setTimeout(() => {
        this.currentVideo = video
        this.cachedRecommendations = video.recommendations
        // for (let i = 0; i < 100; i++) {
        //   this.cachedRecommendations.push({ id: i })
        // }
      }, 1000)
    },
    updateRecommendations () {
      // 0-20 -> 21-... -> 41-...
      var lowerLimit = this.lowerLimit + this.totalLimit + 1
      // ...-20 -> ...-40 -> ...-60
      var upperLimit = this.upperLimit + this.totalLimit

      if (upperLimit > this.cachedRecommendations.length) {
        // Make an API call to refresh the list excluding
        // what was already shown to the user
        this.isLoadingRecommendations = true
        this.lowerLimit = 0
        this.upperLimit = 20
        setTimeout(() => {
          this.isLoadingRecommendations = false
        }, 1000);
      } else {
        this.lowerLimit = lowerLimit
        this.upperLimit = upperLimit
      }
    },
    dropdownClick (params) {
      var index = params[0]
      switch (index) {
        case 0:
          this.showStore = true
          break

        case 2:
          this.showPlaylists = true
          break

        case 3:
          this.showGifts = true
          break

        case 4:
          this.showDonationModal = true
          break

        case 6:
          this.showRecommendationReport = true
          break

        case 7:
          this.showReport = true
          break

        default:
          console.log(index)
          break
      }
    }
  }
}
</script>

<style scoped>
.fs-7 {
  font-size: .85rem;
}

.donators {
  width: 80%;
}

.donators .users {
  overflow-x: scroll;
}
</style>
