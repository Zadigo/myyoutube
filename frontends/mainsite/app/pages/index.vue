<template>
  <section id="videos" class="mx-auto">
    <!-- Search -->
    <u-card class="shadow-sm">
      <form class="grid gap-2 grid-cols-1 xl:grid-cols-4" @submit.prevent>
        <volt-input-text v-model="search" placeholder="Search" class="col-span-1 xl:col-span-3" />
        <volt-select v-model="category" :options="mainCategoriesSelect" class="col-span-1 xl:col-span-2" option-label="name" placeholder="Categories" />
        <volt-select v-model="videoLength" :options="videoLengthSelect" class="col-span-1 xl:col-span-1" option-label="name" placeholder="Video length" />
        <volt-select v-model="uploadDate" :options="uploadDateSelect" class="col-span-1 xl:col-span-1" option-label="name" placeholder="Upload date" />
      </form>
    </u-card>

    <!-- Content -->
    <section id="content" class="mt-5">
      <div class="pt-2 pb-5 flex justify-end">
        <volt-dropdown id="sort-by" :items="sortByMenuItems">
          <template #default="{ attrs }">
            <u-button @click="attrs.toggle">
              <icon name="i-fa7-solid:sort" /> Sort by
            </u-button>
          </template>
        </volt-dropdown>
      </div>

      <!-- Feed -->
      <suspense>
        <template #default>
          <async-feed-component />
        </template>

        <template #fallback>
          <div class="grid grid-cols-4 auto-rows-min gap-2">
            <div v-for="i in 28" :key="i">
              <volt-skeleton height="150px" />
              <volt-skeleton class="mt-1" height="20px" width="30%" />
            </div>
          </div>
        </template>
      </suspense>
    </section>
  </section>
</template>

<script setup lang="ts">
import { defineAsyncComponent } from 'vue'

const AsyncFeedComponent = defineAsyncComponent({
  loader: () => import('~/components/BaseAsyncFeed.vue')
})
console.log('AsyncFeedComponent', AsyncFeedComponent)

/**
 * Menu items
 */

const { menuItems: mainCategoriesSelect } = useMenuItems(Array.from(DEFAULT_MAIN_CATEGORIES))
const { menuItems: videoLengthSelect } = useMenuItems(Array.from(DEFAULT_VIDEO_LENGTH))
const { menuItems: uploadDateSelect } = useMenuItems(Array.from(DEFAULT_UPLOAD_DATE))

/**
 * Search
 */

// useFeedComposable()
const { search, uploadDate, videoLength, category, sortBy } = await useSearchFeedComposable()

/**
 * Sort by menu items
 */

const sortByMenuItems: Arrayable<DefaultSortByMenuItem> = [
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
