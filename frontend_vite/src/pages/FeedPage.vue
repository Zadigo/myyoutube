<template>
  <section id="videos">
    <header class="card shadow-sm">
      <div class="card-body">
        Something
      </div>
    </header>

    <section id="content" class="mt-5">
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
    </section>
  </section>
</template>

<script>
import { useFeed } from '../store/feed'
import { storeToRefs } from 'pinia'

export default {
  name: 'FeedPage',
  setup () {
    const store = useFeed()
    const { videos } = storeToRefs(store)

    return {
      videos
    }
  },
  beforeMount () {
    this.requestVideos()
  },
  methods: {
    async requestVideos () {
      try {
        const response = await this.$client.post('/videos/list')
        this.videos = response.data
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>
