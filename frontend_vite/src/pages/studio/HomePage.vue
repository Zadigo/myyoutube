<template>
  <section id="studio">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-header">
            <div class="d-flex justify-content-between gap-4 align-items-center">
              <div class="actions">
                <v-btn :to="{ name: 'my_studio_upload' }" class="me-2" color="primary" rounded="xl">
                  <font-awesome-icon :icon="['fas', 'fa-upload']" class="me-2" />
                  Upload
                </v-btn>

                <v-btn color="primary" rounded="xl">
                  <font-awesome-icon :icon="['fas', 'fa-chart-simple']" class="me-2" />
                  Statistics
                </v-btn>
              </div>

              <v-form id="search" style="width:30%;" @submit.prevent>
                <v-text-field v-model="search" placeholder="Search" aria-placeholder="Search" variant="outlined" hide-details></v-text-field>
              </v-form>
            </div>
          </div>

          <div class="card-body">
            <div class="list-group">
              <article v-for="video in searchedVideos" :key="video" :aria-label="video" class="list-group-item list-group-item-action p-4 d-flex gap-4 justify-content-left align-items-center">
                <img src="https://via.placeholder.com/100x100" class="img-fluid rounded" alt="">

                <div class="infos p-2 mx-1 flex-shrink-1">
                  <h5>
                    {{ video.title }}
                    <!-- <router-link :to="{ name: 'edit_my_studio_video', params: { id: video.video_id } }">
                    </router-link> -->
                  </h5>

                  <p class="mb-2"> Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ratione error alias voluptatibus doloremque adipisci, inventore quas? Ipsum commodi </p>
                  <p class="d-flex justify-content-left text-muted"><span>4456 vues</span> - <span class="mx-2">400 likes</span></p>
                </div>

                <div class="actions">
                  <v-btn color="primary" rounded="xl">
                    <font-awesome-icon :icon="['fas', 'fa-pen']" />
                  </v-btn>

                  <v-btn color="primary" rounded="xl">
                    <font-awesome-icon :icon="['fas', 'fa-ellipsis-vertical']" />
                  </v-btn>
                </div>
              </article>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import _ from 'lodash'
import { ref } from 'vue'

export default {
  name: 'StudioPage',
  setup () {
    const userVideos = ref([1, 2])
    const search = ref(null)

    return {
      search,
      userVideos
    }
  },
  computed: {
    searchedVideos () {
      if (this.search) {
        return _.filter(this.userVideos, (video) => {
          return video.title.toLowerCase().includes(this.search.toLowerCase())
        })
      } else {
        return this.userVideos
      }
    }
  },
  created () {
    this.requestUserVideos()
  },
  methods: {
    async requestUserVideos () {
      // Get all the details for the current video
      try {
        const response = await this.$client.get(`videos/studio/videos`)
        this.userVideos = response.data
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>
