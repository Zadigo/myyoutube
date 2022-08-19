<template>
  <section id="fast">
    <div class="row">
      <short-video-card v-for="i in 2" :key="i" :video-source="`${i}`" class="mb-2" />
    </div>
  </section>
</template>

<script>
import ShortVideoCard from '@/components/youtube/ShortVideoCard.vue'

export default {
  name: 'ListView',
  components: {
    ShortVideoCard
}
}
</script>
