<template>
  <base-site>
    <section id="for-you-page">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12">
            <div class="card mb-4">
              <div class="card-body">
                <button type="button" class="btn btn-primary shadow-none me-2">
                  <font-awesome-icon icon="fa-solid fa-filter" class="me-2"></font-awesome-icon>
                  Filter
                </button>

                <div class="btn-group ms-auto shadow-none">
                  <button type="button" :class="[showLongVideosTimeline ? 'active' : null ]" class="btn btn-light" @click="showLongVideosTimeline = true">Long</button>
                  <button type="button" :class="[showLongVideosTimeline ? null : 'active' ]" class="btn btn-light" @click="showLongVideosTimeline = false">Shorts</button>
                </div>
              </div>

              <div class="card-footer">
                <input type="text" class="form-control mb-2" placeholder="Search categories" multiple>
                <div class="d-flex justify-content-around">
                  <select class="form-select" aria-label="Default select example">
                    <option selected>Date de mise en ligne</option>
                    <option value="1">Nombres de vues</option>
                    <option value="2">Avis</option>
                    <option value="3">Three</option>
                  </select>

                  <select class="form-select mx-2" aria-label="Default select example">
                    <option selected>Vidéo</option>
                    <option value="1">Chaînes</option>
                    <option value="2">Playlist</option>
                  </select>

                  <select class="form-select" aria-label="Default select example">
                    <option selected>Entre 4 et 20 minutes</option>
                    <option selected>Plus de 20 minutes</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>

        <section v-if="showLongVideosTimeline" class="row">
          <div class="col-12">
            <div class="row">
              <div v-for="card in 8" :key="card" class="col-3 mb-2">
                <article class="card shadow-sm text-dark">
                  <router-link :to="{ name: 'video_view' }">
                    <img src="https://via.placeholder.com/800" class="card-img" alt="">
                  </router-link>

                  <div class="card-body d-flex justify-content-left">
                    <div id="avatar">
                      <router-link :to="{ name: 'channel_view' }">
                        <img :src="require('@/assets/avatar1.png')" class="img-fluid rounded-circle" width="50" alt="">
                      </router-link>
                    </div>

                    <div class="ms-4">
                      <h5>Some video</h5>
                      <router-link :to="{ name: 'channel_view' }">
                        <p class="mb-1 text-muted">Jubilee</p>
                        <p class="text-muted">{{ formatSubscribers(15395) }} views - 3 hours ago</p>
                      </router-link>
                    </div>
                  </div>
                </article>
              </div>
            </div>

            <hr class="my-4">

            <div class="row">
              <h3 class="fw-bold">Some recommended section</h3>
              <div v-for="card in 8" :key="card" class="col-3 mb-2">
                <router-link :to="{ name: 'video_view' }">
                  <article class="card shadow-sm text-dark">
                    <img src="https://via.placeholder.com/800" class="card-img" alt="">

                    <div class="card-body d-flex justify-content-left">
                      <div id="avatar">
                        <img :src="require('@/assets/avatar1.png')" class="img-fluid rounded-circle" width="50" alt="">
                      </div>

                      <div class="ms-4">
                        <h5>Some video</h5>
                        <p class="mb-1 text-muted">Jubilee</p>
                        <p class="text-muted">{{ formatSubscribers(15395) }} views - 3 hours ago</p>
                      </div>
                    </div>
                  </article>
                </router-link>
              </div>
            </div>
          </div>
        </section>
      </div>
    </section>
  </base-site>
</template>

<script>
import BaseSite from '@/layouts/BaseSite.vue'
import useFormatting  from '@/composables/formatting'

export default {
  name: 'TimelinePageView',
  components: {
    BaseSite
  },
  setup () {
    const { formatSubscribers } = useFormatting()
    return {
      formatSubscribers
    }
  },
  data () {
    return {
      showLongVideosTimeline: true
    }
  }
}
</script>
