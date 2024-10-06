<template>
  <div class="row">
    <div v-for="video in videos" :key="video.id" class="col-3 my-1">
      <router-link :to="{ name: 'video_details', params: { id: video.video_id } }" :data-id="video.video_id">
        <article class="card shadow-sm" :aria-label="video.title">
          <div class="card-body">
            <h1 class="h4 card-title">{{ video.title }}</h1>
          </div>
        </article>
      </router-link>
    </div>
  </div>
</template>

<script>
// import { ref } from 'vue'
import { useFeed } from 'src/store/feed'
import { storeToRefs } from 'pinia'
import { client } from 'src/plugins/axios'

export default {
  name: 'AsyncFeed',
  emits: {
    'feed-loaded' () {
      return true
    }
  },
  async setup () {
    // const videos = ref([])
    const feedStore = useFeed()
    const { videos } = storeToRefs(feedStore)

    async function requestVideos () {
      // Returns all the videos based on personnalized
      // recommendations for the feed
      try {
        const response = await client.post('/videos/')
        feedStore.videos = response.data
      } catch (e) {
        console.log(e)
      }
    }
    await requestVideos()

    return {
      requestVideos,
      videos
    }
  },
  mounted() {
    this.$emit('feed-loaded', this.videos)
  }
}
</script>
