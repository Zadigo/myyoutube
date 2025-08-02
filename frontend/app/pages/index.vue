<template>
  <section id="videos" class="container px-5">
    <VoltCard>
      <template #content>
        <form class="space-y-2" @submit.prevent>
          <VoltInputText type="search" placeholder="Search" class="w-2/5" />
          
          <div class="flex justify-around gap-2">
            <VoltSelect :options="defaultMainCategories.map(x => ({ name: x }))" class="w-full" option-label="name" placeholder="Categories" />
            <VoltSelect :options="defaultVideoLength.map(x => ({ name: x }))" class="w-full" option-label="name" placeholder="Video length" />
            <VoltSelect :options="defaultUploadDate.map(x => ({ name: x }))" class="w-full" option-label="name" placeholder="Upload date" />
          </div>
        </form>
      </template>

      <template #footer>
        <VoltButton>
          <font-awesome icon="sort" /> Sort by: 
        </VoltButton>
      </template>
    </VoltCard>

    <section id="content" class="mt-5">
      <Suspense>
        <template #default>
          <AsyncFeedComponent />
        </template>

        <template #fallback>
          <div class="grid grid-cols-4 auto-rows-min gap-2">
            <div v-for="i in 28" :key="i">
              <VoltSkeleton class="h-[200px]" />
            </div>
          </div>
        </template>
      </Suspense>
    </section>
  </section>
</template>

<script setup lang="ts">
import { defineAsyncComponent } from 'vue'
import { defaultVideoLength, defaultMainCategories, defaultUploadDate } from '~/apps/data'

const AsyncFeedComponent = defineAsyncComponent({
  loader: () => import('~/apps/components/BaseAsyncFeed.vue')
})
</script>
