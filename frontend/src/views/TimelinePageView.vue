<template>
  <base-site>
    <section id="for-you-page">
      <div class="container-fluid">
        <div class="row">
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
  }
}
</script>
