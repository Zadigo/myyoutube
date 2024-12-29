<template>
  <section id="videos">
    <header class="card shadow-sm">
      <div class="card-body">
        Filters
      </div>
    </header>

    <section id="content" class="mt-5">
      <Suspense>
        <template #default>
          <AsyncFeedComponent />
        </template>

        <template #fallback>
          <BaseSkeleton :loading="true" />
        </template>
      </Suspense>
    </section>
  </section>
</template>

<script setup>
// import { useFeed } from '~/stores/feed';
// import { storeToRefs } from 'pinia';
import { defineAsyncComponent } from 'vue';

// const store = useFeed()
// const { videos } = storeToRefs(store)

const AsyncFeedComponent = defineAsyncComponent({
  loader: () => import('~/components/BaseAsyncFeed.vue')
})
</script>
