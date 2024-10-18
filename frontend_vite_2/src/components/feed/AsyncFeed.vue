<template>
  <div v-if="videos.length" class="row">
    <div v-for="video in videos" :key="video.id" class="col-3 my-1">
      <router-link :to="{ name: 'video_details', params: { id: video.video_id } }" :data-id="video.video_id">
        <article class="card shadow-sm" :aria-label="video.title">
          <div class="card-body">
            <h1 class="h4 card-title">
              {{ video.title }}
            </h1>
          </div>
        </article>
      </router-link>
    </div>
  </div>

  <div v-else class="row">
    <h2>No videos</h2>
  </div>
</template>

<script lang="ts">
import { client } from '@/plugins/axios';
import { useFeed } from '@/store/feed';
import { VideosFeedResponseData } from '@/types/feed';
import { storeToRefs } from 'pinia';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'AsyncFeed',
  emits: {
    'feed-loaded' (_videos: VideosFeedResponseData[]) {
      return true
    }
  },
  async setup () {
    const feedStore = useFeed()
    const { videos } = storeToRefs(feedStore)

    async function requestVideos () {
      try {
        const response = await client.get<VideosFeedResponseData>('/videos/')
        feedStore.videos = response.data
      } catch (e) {
        // Handle error
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
})
</script>
