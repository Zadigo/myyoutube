<template>
  <section id="videos" class="container mx-auto px-4">
    <!-- Header -->
    <VoltCard class="shadow-sm">
      <template #content>
        <form @submit.prevent>
          <VoltInputText v-model="search" placeholder="Search" class="w-2/5" />

          <div class="flex justify-around gap-2 mt-3">
            <VoltSelect v-model="category" :options="mainCategoriesSelect" class="w-full" option-label="name" placeholder="Categories" />
            <VoltSelect v-model="videoLength" :options="videoLengthSelect" class="w-full" option-label="name" placeholder="Video length" />
            <VoltSelect v-model="uploadDate" :options="uploadDateSelect" class="w-full" option-label="name" placeholder="Upload date" />
          </div>
        </form>
      </template>
    </VoltCard>

    <!-- Content -->
    <section id="content" class="mt-5">
      <div class="pt-2 pb-5 flex justify-end">
        <VoltDropdownButton id="sort-by" :items="sortByMenuItems">
          <Icon name="i-fa7-solid:sort" /> Sort by
        </VoltDropdownButton>
      </div>

      <Suspense>
        <AsyncFeedComponent />

        <template #fallback>
          <div class="grid grid-cols-4 auto-rows-min gap-2">
            <div v-for="i in 28" :key="i">
              <VoltSkeleton height="150px" />
              <VoltSkeleton class="mt-1" height="20px" width="30%" />
            </div>
          </div>
        </template>
      </Suspense>
    </section>
  </section>
</template>

<script setup lang="ts">
import { defineAsyncComponent } from 'vue'
import { useFeedComposable, useMenuItems } from '~/composables/use'
import { defaultMainCategories, defaultUploadDate, defaultVideoLength } from '~/data'

import type { DefaultSortByMenuItem } from '~/data'

const AsyncFeedComponent = defineAsyncComponent({
  loader: () => import('~/components/BaseAsyncFeed.vue')
})

/**
 * Menu items
 */

const { menuItems: mainCategoriesSelect } = useMenuItems(Array.from(defaultMainCategories))
const { menuItems: videoLengthSelect } = useMenuItems(Array.from(defaultVideoLength))
const { menuItems: uploadDateSelect } = useMenuItems(Array.from(defaultUploadDate))

// const feedStore = useFeedStore()
// const { search, uploadDate, videoLength, category,  sortBy } = storeToRefs(feedStore)

const { search, uploadDate, videoLength, category, sortBy } = await useFeedComposable()

/**
 * Sort by menu items
 */

const sortByMenuItems: DefaultSortByMenuItem[] = [
  {
    label: 'Upload date',
    icon: 'i-fa7-solid:clock',
    command: () => {
      sortBy.value = 'Upload date'
    }
  },
  {
    label: 'View count',
    icon: 'i-fa7-solid:eye',
    command: () => {
      sortBy.value = 'View count'
    }
  },
  {
    label: 'Rating',
    icon: 'i-fa7-solid:star',
    command: () => {
      sortBy.value = 'Rating'
    }
  }
]
</script>
