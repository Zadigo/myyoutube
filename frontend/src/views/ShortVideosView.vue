<template>
  <base-site>
    <section id="fast">
      <div class="row">
        <short-video-card v-for="i in 3" :key="i" class="mb-2" />
      </div>
    </section>
  </base-site>
</template>

<script>
import ShortVideoCard from '@/components/youtube/ShortVideoCard.vue'
import BaseSite from '@/layouts/BaseSite.vue';

export default {
  name: 'ShortVideos',
  components: {
    ShortVideoCard,
    BaseSite
}
}
</script>
