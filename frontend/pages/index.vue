<template>
  <section id="videos" class="container px-5">
    <header class="card shadow-sm">
      <v-form class="card-body" @submit.prevent>
        <v-text-field variant="solo-filled" type="search" placeholder="Search" flat />
        
        <div class="d-flex gap-2">
          <v-select :items="[1, 2]" placeholder="Categories" variant="solo-filled" flat />
          <v-select :items="videoLength" placeholder="Video length" variant="solo-filled" flat />
          <v-select :items="uploadDate" placeholder="Upload date" variant="solo-filled" flat />
        </div>

        <v-btn variant="tonal" color="light">
          <font-awesome icon="sort" /> Sort by: 
        </v-btn>
      </v-form>
    </header>

    <section id="content" class="mt-5">
      <Suspense>
        <template #default>
          <AsyncFeedComponent />
        </template>

        <template #fallback>
          <div class="row">
            <div v-for="i in 30" :key="i" class="col-3">
              <BaseSkeleton :loading="true" height="30px" />
            </div>
          </div>
        </template>
      </Suspense>
    </section>
  </section>
</template>

<script setup lang="ts">
import { defineAsyncComponent } from 'vue';

const AsyncFeedComponent = defineAsyncComponent({
  loader: () => import('~/components/BaseAsyncFeed.vue')
})

const sortBy = [
  'Upload date',
  'View count',
  'Rating'
]

const videoLength = [
  'Under 4 minutes',
  '4-20 minutes',
  'Over 20 minutes'
]

const uploadDate = [
  'Last hour',
  'Today',
  'This week',
  'This month',
  'This year'
]
</script>
