<template>
  <div class="row">
    <h3 v-if="title" class="fw-bold">Some recommended section</h3>

    <div v-for="card in 8" :key="card" class="col-3 mb-2">
      <article class="card shadow-sm text-dark">
        <router-link :to="{ name: 'video_view' }">
          <img :src="require('@/assets/cover.jpg')" class="card-img shadow rounded" alt="Some recommended section">
        </router-link>

        <div class="card-body d-flex justify-content-left">
          <div id="avatar">
            <router-link :to="{ name: 'channel_view' }">
              <img :src="require('@/assets/avatar1.png')" class="img-fluid rounded-circle" width="50" alt="">
            </router-link>
          </div>

          <div class="ms-4">
            <h6 class="fw-bold">Some video</h6>
            <router-link :to="{ name: 'channel_view' }">
              <p class="mb-1 text-muted">Jubilee</p>
              <p class="text-muted m-0">{{ formatSubscribers(15395) }} views - 3 hours ago</p>
            </router-link>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
import useFormatting from '@/composables/formatting'

export default {
  name: 'VideoSection',
  props: {
    title: {
      type: String,
      required: false
    }
  },
  setup () {
    const { formatSubscribers } = useFormatting()
    return {
      formatSubscribers
    }
  }
}
</script>

<style scoped>
article img {
  transition: all .3s ease-in-out;
}
article img:hover {
  transform: scale(1.3, 1.3);
}
article:hover {
  z-index: 1000;
}
</style>
