<template>
  <base-site-vue>
    <section id="youtube">
      <div class="container-fluid p-0">
        <!-- Player -->
        <base-video-player-vue :video-url="require('@/assets/video1.mp4')"></base-video-player-vue>

        <div class="position-relative">
          <!-- Information -->
          <div class="row">
            <div class="col-12">
              <div class="card mt-2">
                <div class="card-body">
                  <h5 class="card-title">
                    {{ currentVideo.title }}
                  </h5>

                  <div :class="{ 'flex-column': breakpoints.isSmaller('md') }" class="d-flex justify-content-between">
                    <span :class="{ 'mb-2': breakpoints.isSmaller('md') }" class="text-muted">
                      {{ currentVideo.views }} views - {{ currentVideo.created_on }}
                    </span>

                    <!-- Actions -->
                    <div class="d-flex justify-content-around">
                      <div class="btn-group">
                        <button type="button" class="btn btn-lg btn-primary" @click="likeVideo">
                          <span class="mdi mdi-thumb-up me-2"></span>{{ currentVideo.likes }}
                        </button>

                        <button type="button" class="btn btn-lg btn-primary" @click="likeVideo">
                          <span class="mdi mdi-thumb-down me-2"></span>{{ currentVideo.dislikes }}
                        </button>
                      </div>

                      <base-dropdown-button-vue :button-name="'More'" :color="'secondary'" :items="[{ name: 'Store', icon: 'store' }, { name: 'Download', icon: 'download' }, { name: 'Save', icon: 'content-save' }, { name: 'Gift', icon: 'gift' }, { name: 'Donate', icon: 'cash' }, { name: 'Share', icon: 'share' }, { name: 'Recommendation', icon: 'star-remove-outline' }, { name: 'Report', icon: 'alert' }]" class="mx-2" @dropdown-click="dropdownClick" />

                      <div class="btn-group">
                        <button type="button" class="btn btn-primary btn-lg" @click="currentVideo.channel.subscribed = !currentVideo.channel.subscribed">
                          <span v-if="currentVideo.channel.subscribed">Unsubscribe</span>
                          <span v-else>Subscribe</span>
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

              <div class="card my-2">
                <div class="card-body">
                  <div class="row">
                    <div class="col-2">
                      <img src="http://via.placeholder.com/100x100" class="img-fluid rounded-circle" alt="Image 6">
                    </div>

                    <div class="col-10">
                      <router-link :to="{ name: 'home_view' }" class="fw-bold mb-0">
                        {{ currentVideo.channel.name }}
                        <font-awesome-icon v-if="currentVideo.channel.verified" icon="fa-solid fa-circle-check" class="text-primary mx-1" />
                      </router-link>

                      <p class="text-muted fw-light m-0">{{ formatSubscribers(currentVideo.channel.subscribers) }} subscribers</p>

                      <base-scrollbar-vue :items="currentVideo.categories" class="my-3" />

                      <p id="description">
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
            </div>
          </div>

          <div class="row">
            <!-- Comments -->
            <comment-section :current-video="currentVideo" />

            <!-- Recommendations -->
            <div v-if="breakpoints.isGreater('sm')" class="col-sm-12 col-md-4">
              <div class="card mb-3">
                <div class="card-body">
                  <div class="d-flex justify-content-between">
                    <button type="button" class="btn btn-sm btn-secondary btn-rounded shadow-none" @click="updateRecommendations">
                      <span class="mdi mdi-reload me-2"></span>
                      Load more
                    </button>

                    <router-link :to="{ name: 'home_view' }" class="btn btn-sm btn-secondary btn-rounded shadow-none">
                      <span class="mdi mdi-expand-all me-2"></span>
                      See all
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

            <recommendation-drawer-vue v-else :show="showRecommendationsDrawer" :recommendations="recommendations" />
          </div>
        </div>
      </div>

      <!-- Modals -->
      <base-modal-vue id="donation" :show="showDonationModal" title="Make a donation" @close="showDonationModal = false">
        <div class="row">
          <div class="col-12">
            <div class="alert alert-info">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque minima
              ipsam placeat est ex? Doloremque, nemo architecto provident necessitatibus
              sequi modi dolorem! Ab rem inventore esse libero laudantium animi dicta!
            </div>

            <div class="col-12">
              <input type="number" min="0" max="100" step="5" class="form-control">

              <div class="form-check form-switch my-2">
                <input id="super-donation" class="form-check-input" type="checkbox" role="switch" />
                <label class="form-check-label" for="super-donation">
                  Make a super donation
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
              Send - $15
            </button>
          </div>
        </template>
      </base-modal-vue>

      <base-modal-vue id="store" :show="showStore" :scrollable="true" size="xl" @close="showStore = false">
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
                    <button type="button" class="btn btn-primary btn-sm">Add to cart</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </base-modal-vue>

      <base-modal-vue id="gift" :show="showGifts" :scrollable="true" size="sm" @close="showGifts = false">
        <div class="row">
          <div class="col-12">
            <div class="alert alert-danger">
              You have purchased no gifts yet. You can buy
              gifts here before pursuing.
            </div>

            <div class="list-group">
              <a v-for="i in 10" :key="i" href class="list-group-item d-flex justify-content-between" @click.prevent>
                <span>Gift {{ i }}</span>
                <div class="btn-group shadow-none">
                  <button type="button" class="btn btn-sm btn-primary">
                    Donate
                  </button>
                </div>
              </a>
            </div>
          </div>
        </div>
      </base-modal-vue>

      <base-modal-vue id="report" :show="showReport" :scrollable="true" size="sm" title="Report video" @close="showReport = false">
        <div class="row">
          <div class="col-12">
            <base-accordion-vue :items="reports" />
          </div>

          <div class="col-12 my-4">
            <p class="mb-1">Flag the section you believe to be problematic</p>
            <div class="d-flex justify-content-between">
              <input type="text" class="form-control p-2">
              <input type="text" class="form-control p-2 ms-2">
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
              Send
            </button>
          </div>
        </template>
      </base-modal-vue>

      <base-offcanvas-vue id="playlists" :show="showPlaylists" title="Playlists" position="end" @close="showPlaylists = false">
        <div class="list-group">
          <a v-for="i in 5" :key="i" href class="list-group-item d-flex justify-content-between" @click.prevent>
            <div class="form-check my-2">
              <input id="flexCheckChecked" class="form-check-input" type="checkbox">
              <label class="form-check-label" for="flexCheckChecked">
                {{ i }}
              </label>
            </div>
          </a>
        </div>
      </base-offcanvas-vue>

      <base-offcanvas-vue id="recommendation" :show="showRecommendationReport" title="Recommendation" position="end" @close="showRecommendationReport = false">
        <div class="row">
          <div class="col-12">
            <div class="alert alert-warning">
              You can use this tool to signal that this video was not properly categorized
              by the creator and therefore does not correspond to a result you expected
            </div>

            <div class="list-group my-3">
              <div class="list-group-item">
                <div class="form-check form-switch">
                  <input id="wrong-category-alert" class="form-check-input" type="checkbox" role="switch" />
                  <label class="form-check-label" for="wrong-category-alert">
                    This video is not in the proper category
                  </label>
                </div>
              </div>
            </div>

            <select class="form-select" aria-label="Expected category">
              <option selected>Expected category</option>
              <option value="1">One</option>
              <option value="2">Two</option>
              <option value="3">Three</option>
            </select>

            <div class="list-group mt-3">
              <div class="list-group-item">
                <div class="form-check form-switch">
                  <input id="block-channel" class="form-check-input" type="checkbox" role="switch" />
                  <label class="form-check-label" for="block-channel">
                    Block this channel
                  </label>
                </div>
              </div>
            </div>
          </div>
        </div>

        <template #footer>
          <div class="offcanvas-footer">
            <button type="button" class="btn btn-outline-danger" @click="showRecommendationReport = false">
              Close
            </button>

            <button type="button" class="btn btn-primary ms-2">
              Save
            </button>
          </div>
        </template>
      </base-offcanvas-vue>
    </section>

    <hr class="my-5">

    <h1>Page set algorithm</h1>
    <section id="algorithm">
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-12 col-md-8">
            <div class="card">
              <div class="card-body">
                <p class="alert alert-info">
                  If no options are selected, YouTube will use your viewing history
                  to recommend the most relevant videos
                </p>
                <div class="form-check form-switch my-4">
                  <input id="recommendation-preference" class="form-check-input" type="checkbox" role="switch" />
                  <label class="form-check-label" for="recommendation-preference">
                    Let YouTube decide which are the most relevant videos for me
                  </label>
                </div>

                <div class="card shadow-none">
                  <div class="card-body">
                    <label for="categories">Select the categories for which you will have the most interest</label>
                    <input type="text" class="form-control p-2" placeholder="Categories" name="categories">
                    <input type="text" class="form-control p-2 my-2" placeholder="Subcategories" name="subcategories" disabled>

                    <div class="list-group list-group-flush">
                      <div class="list-group-item ps-0">
                        <div class="form-check form-switch">
                          <input id="recommend-from-current" class="form-check-input" type="checkbox" role="switch" />
                          <label class="form-check-label" for="recommend-from-current">
                            Let YouTube recommend the most popular videos from what
                            users have also watched based on the video that you
                            are currently viewing
                          </label>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="col-sm-12 col-md-4">
            <div class="card">
              <div class="card-header">
                <h3>Preferred categories</h3>
              </div>

              <div class="card-body">
                <h4 class="fw-bold h5 mb-1">Sports</h4>
                <div class="list-group my-3">
                  <a class="list-group-item list-group-item-action d-flex justify-content-between">
                    <span>WNBA</span>
                    <button type="button" class="btn btn-sm btn-rounded btn-dark shadow-none">
                      <span class="mdi mdi-delete"></span>
                    </button>
                  </a>
                </div>
              </div>

              <div class="card-footer text-right">
                <button type="button" class="btn btn-danger">
                  <span class="mdi mdi-delete-sweep"></span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <hr class="my-5">

    <h1>Page user's channel</h1>
    <section id="channel" class="bg-dark">
      <div class="shadow channel-header">
        <base-carousel />

        <div class="channel-actions">
          <div class="d-flex justify-content-left align-items-center">
            <h3 class="display-6 fw-bold text-light me-3">My channel name</h3>
            <font-awesome-icon icon="fa-solid fa-circle-check" class="text-white" />
          </div>
          <p class="fw-light text-light">310 vidéos</p>
          <button type="button" class="btn btn-primary">
            Subscribe
          </button>
        </div>
      </div>

      <div class="container">
        <section class="row p-4">
          <!-- TODO: This will be a component in order to iterate
          over each video sections -->
          <div v-for="i in 2" :key="i" class="col-12 my-2">
            <div class="fw-bold h5 text-white mt-4"><span class="text-primary">Prime Amazon</span> Originals and Exclusives <a href>See more</a></div>
            <div class="row">
              <video-card-vue v-for="i in 4" :key="i" class="gx-1" />
            </div>
          </div>
        </section>
      </div>
    </section>

    <hr class="my-5">

    <h1>Short videos</h1>
    <section id="fast">
      <div class="row">
        <short-video-card />
      </div>
    </section>

    <hr class="my-5">

    <h1>Short video</h1>
    <section id="fast" style="height:100vh;">
      <div class="row gx-0">
        <div class="col-7 bg-dark">
          <div class="h-100 w-50 z-index-1 mx-auto">
            <img src="https://via.placeholder.com/400x700" class="img-fluid" alt="">
          </div>
        </div>

        <div class="col-5">
          <div class="user-info p-3 border-bottom">
            <!-- TODO: Use reusable user component info here -->
            <div class="row mb-4">
              <div class="col-2">
                <a href>
                  <img src="https://via.placeholder.com/400x400" class="img-fluid z-depth-1 rounded-circle" alt="">
                </a>
              </div>

              <div class="col-10 position-relative">
                <div class="d-flex justify-content-left" @mouseenter="showUserInfo = true" @mouseleave="showUserInfo = false">
                  <a href class="me-2">
                    <span class="fw-bold">
                      camillembaye
                    </span>
                  </a>
                  <p class="fw-light m-0">Camille Mbaye</p>
                </div>
                <button type="button" class="btn btn-outline-primary">
                  Subscribe
                </button>
              </div>
            </div>

            <div class="row">
              <div class="col-8 align d-flex justify-content-left align-items-center">
                <button type="button" class="btn btn-floating btn-light shadow-none mb-2 btn-lg me-1">
                  <font-awesome-icon :class="[true ? 'text-danger' : null]" icon="fa-solid fa-heart" />
                </button>
                <span class="fw-bold fs-small text-muted me-2">15.5.k</span>

                <button type="button" class="btn btn-floating btn-light shadow-none mb-2 btn-lg">
                  <font-awesome-icon icon="fa-solid fa-message" />
                </button>
              </div>
            </div>
          </div>

          <div class="comments p-3 bg-light" style="overflow-y: scroll; height:300px;">
            <template v-for="i in 100" :key="i">
              <div :class="[i > 0 ? 'mb-1' : null]" class="card">
                <div class="card-body">
                  <div class="d-flex justify-content-around">
                    <div class="col-2 me-3">
                      <img src="http://via.placeholder.com/100x100" class="img-fluid rounded-circle" alt="Image 1">
                    </div>

                    <div clas="col-11 ms-1">
                      <div class="d-flex justify-content-left">
                        <span class="fw-bold me-2">User</span>
                        <span class="text-muted">3 weeks ago</span>
                      </div>

                      <p class="card-text">
                        I can’t stop smiling. I once “borrowed “ my brother’s shoes and accidentally ran into him
                        and his friends. The whole time i was talking to them his eyes were laser focused on the shoes. I tried
                        cutting the conversation short but at some point he leaned closer and went “ is that my
                        shoes“. He roasted me but it was all lighthearted and fun. I can totally relate to the
                        sisters
                      </p>

                      <div class="btn-group shadow-none">
                        <button type="button" class="btn btn-primary btn-sm shadow-none">Report</button>
                        <button type="button" class="btn btn-info btn-sm shadow-none">Reply</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </template>
          </div>

          <div class="actions p-3 border-top">
            <input type="text" class="form-control p-2">
          </div>
        </div>
      </div>
    </section>
  </base-site-vue>
</template>

<script>
import reports from '@/data/reports'
import video from '@/data/video'

import { ref, provide } from 'vue'

// import BaseDropGroupVue from '@/layouts/BaseDropGroup.vue'
import BaseCarousel from '@/layouts/BaseCarousel.vue'
import BaseVideoPlayerVue from '../layouts/BaseVideoPlayer.vue'
import BaseScrollbarVue from '../layouts/BaseScrollbar.vue'
import BaseDropdownButtonVue from '@/layouts/BaseDropdownButton.vue'
import BaseModalVue from '@/layouts/BaseModal.vue'
import BaseOffcanvasVue from '@/layouts/BaseOffcanvas.vue'
import BaseAccordionVue from '@/layouts/BaseAccordion.vue'
import CommentSection from '@/components/youtube/CommentSection.vue'
import BaseSiteVue from '../layouts/BaseSite.vue'
import RecommendationDrawerVue from '../components/youtube/RecommendationDrawer.vue'
import ListRecommendationsVue from '@/components/youtube/ListRecommendations.vue'
import VideoCardVue from '@/components/youtube/channel/VideoCard.vue'

import { breakpointsTailwind, useBreakpoints } from '@vueuse/core'
import ShortVideoCard from '@/components/youtube/ShortVideoCard.vue'
import useFormatting from '@/composables/formatting'

export default {
  name: 'YoutubeTemplate',
  components: {
    BaseCarousel,
    BaseVideoPlayerVue,
    BaseDropdownButtonVue,
    BaseModalVue,
    BaseAccordionVue,
    // BaseDropGroupVue,
    BaseOffcanvasVue,
    BaseScrollbarVue,
    BaseSiteVue,
    CommentSection,
    ListRecommendationsVue,
    RecommendationDrawerVue,
    VideoCardVue,
    ShortVideoCard
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
    // isLoading: true,
    isLoadingRecommendations: true,

    showDonationModal: false,
    showPlaylists: false,
    showStore: false,
    showGifts: false,
    showReport: false,
    showRecommendationReport: false,
    showRecommendationsDrawer: false,

    sortMethod: 'Newest',

    currentVideo: video,

    lowerLimit: 0,
    upperLimit: 20,
    totalLimit: 20,
    recommendationLimit: 5,
    cachedRecommendations: [],

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

.channel-header {
  position: relative;
}

.channel-actions {
  position: absolute;
  z-index: 999;
  top: 0;
  left: 0;
  padding: 1rem;
}
</style>
