<template>
  <base-site>
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
  </base-site>
</template>

<script>
import BaseCarousel from '@/layouts/BaseCarousel.vue'
import BaseSite from '@/layouts/BaseSite.vue';
import VideoCardVue from '@/components/youtube/channel/VideoCard.vue'

export default {
  name: 'ChannelView',
  components: {
    BaseCarousel,
    VideoCardVue,
    BaseSite
}
}
</script>

<style scoped>
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
