<template>
  <section id="videos">
    <header class="card shadow-sm">
      <div class="card-body">
        Filters
      </div>
    </header>

    <section id="content" class="mt-5">
      <!-- <div class="row">
        <div v-for="video in videos" :key="video.id" class="col-3 my-1">
          <router-link :to="{ name: 'video_details', params: { id: video.video_id } }" :data-id="video.video_id">
            <article class="card shadow-sm" :aria-label="video.title">
              <div class="card-body">
                <h1 class="h4 card-title">{{ video.title }}</h1>
              </div>
            </article>
          </router-link>
        </div>
      </div> -->

      <suspense>
        <template #default>
          <async-feed-component />
        </template>

        <template #fallback>
          <BaseSkeleton :loading="true" />
        </template>
      </suspense>
    </section>
  </section>
</template>

<script lang="ts">
import { useFeed } from '@/store/feed';
import { storeToRefs } from 'pinia';
import { defineAsyncComponent, defineComponent } from 'vue';

import BaseSkeleton from '@/components/BaseSkeleton.vue';

export default defineComponent({
  name: 'FeedPage',
  components: {
    BaseSkeleton,
    AsyncFeedComponent: defineAsyncComponent({
      loader: () => import('@/components/feed/AsyncFeed.vue')
    })
  },
  setup () {
    const store = useFeed()
    const { videos } = storeToRefs(store)

    return {
      videos
    }
  }
})
</script>
