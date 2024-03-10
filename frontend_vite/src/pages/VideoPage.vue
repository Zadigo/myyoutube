<template>
  <section id="video">
    <section class="row">
      <div class="col-12">
        <base-video-player :video-source="'/video1.mp4'" />
      </div>
    </section>

    <section class="row mt-4">
      <user-video-actions />

      <!-- Information -->
      <div class="col-12 mt-4">
        <div class="card">
          <div class="card-body">
            <div class="d-flex flex-row justify-content-around align-items-start gap-3">
              <img src="/avatar1.png" class="img-fluid rounded-circle" width="120" height="120" alt="">

              <div class="information">
                <v-btn class="px-0" color="primary" variant="plain">
                  <span class="fw-bold">Malika Andrews - ESPN</span>
                  <font-awesome-icon icon="fa fa-circle-check" class="ms-4" />
                </v-btn>
                <p class="text-body-tertiary">345.6K subscribers</p>

                <v-sheet class="mx-auto" max-width="800px">
                  <v-slide-group show-arrows>
                    <v-slide-group-item v-for="n in 10" :key="n" v-slot="{ isSelected, toggle }">
                      <v-btn :color="isSelected ? 'success' : undefined" class="ma-2" rounded @click="toggle">
                        Options {{ n }}
                      </v-btn>
                    </v-slide-group-item>
                  </v-slide-group>
                </v-sheet>

                <p class="fw-light">
                  Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                  Sequi porro iure repellat optio, ipsum ducimus veniam natus
                  ipsam dolor, suscipit distinctio vero? Labore repellendus
                  ipsum et cumque fuga? Ullam, nam! Lorem ipsum dolor sit amet
                  consectetur adipisicing elit. Voluptates id pariatur
                  fuga molestiae aperiam inventore repellendus, dolorum
                  ducimus saepe fugiat minima quisquam. Deleniti, ratione?
                  Quis et harum ullam ab nam.
                </p>

                <v-btn color="primary" variant="plain">
                  <font-awesome-icon icon="fa fa-caret-down" class="me-2" />
                  More
                </v-btn>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="row mt-4">
      <div class="col-8">
        <div class="card">
          <div class="card-body">
            <div class="d-flex align-items-center justify-content-between">
              <h2 class="h4 m-0">6,909 Comments</h2>

              <v-menu>
                <template v-slot:activator="{ props }">
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
          <user-comment-actions />

          <!-- Comments -->
          <user-comment v-for="i in 3" :key="i" />
        </div>
      </div>

      <!-- Recommendations -->
      <div class="col-4">
        <div class="card">
          <div class="card-body"></div>
        </div>

        <recommendation-section />
      </div>
    </section>
  </section>
</template>

<script>
import BaseVideoPlayer from '../components/BaseVideoPlayer.vue'
import UserComment from '../components/video/UserComment.vue'
import UserVideoActions from '../components/video/UserVideoActions.vue'
import UserCommentActions from '../components/video/UserCommentActions.vue'
import { defineAsyncComponent } from 'vue'

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
    RecommendationSection: defineAsyncComponent({
      loader: () => import('../components/video/UserRecommendations.vue'),
      loadingComponent: null,
      delay: 4000,
      errorComponent: null,
      timeout: 5000
    })
  },
  setup () {
    return {
      sortActions
    }
  }
}
</script>
