<template>
  <section id="videos" class="mx-auto">
    <!-- Content -->
    <section id="content" class="mt-5">
      <div class="pt-2 pb-5 flex gap-2 items-center justify-end">
        <u-input v-model="search" :ui="{ trailing: 'pr-0' }" placeholder="Search" class="w-100">
          <template #leading>
            <icon name="i-lucide-search" />
          </template>

          <template #trailing>
            <u-button variant="subtle" @click="() => { toggleShowFilterModal(true) }">
              <icon name="i-lucide-filter" /> More
            </u-button>
          </template>
        </u-input>

        <u-dropdown-menu id="sort-by" :items="SORTBY_MENU_ITEMS">
          <u-button variant="subtle">
            <icon name="i-fa7-solid:sort" /> Sort by
          </u-button>
        </u-dropdown-menu>
      </div>

      <!-- Feed -->
      <suspense>
        <template #default>
          <async-feed-component />
        </template>

        <template #fallback>
          <div class="grid grid-cols-3 auto-rows-min gap-2">
            <div v-for="i in 28" :key="i">
              <u-skeleton class="w-full" />
              <u-skeleton class="mt-1 w-full" />
            </div>
          </div>
        </template>
      </suspense>
    </section>

    <u-modal v-model:open="showFilterModal">
      <template #title>
        Filter Videos
      </template>

      <template #body>
        <form @submit.prevent>
          <u-select-menu v-model="category" :items="DEFAULT_CATEGORIES_SELECT_ITEMS" class="w-full" placeholder="Categories" multiple />
          <div class="flex gap-2 my-2">
            <u-select v-model="videoLength" :items="DEFAULT_VIDEO_LENGTH_SELECT_ITEMS" placeholder="Video length" />
            <u-select v-model="uploadDate" :items="DEFAULT_UPLOAD_DATE_SELECT_ITEMS" placeholder="Upload date" />
          </div>
        </form>
      </template>
    </u-modal>
  </section>
</template>

<script setup lang="ts">
import { defineAsyncComponent } from 'vue'
import type { DropdownMenuItem } from '@nuxt/ui'

const AsyncFeedComponent = defineAsyncComponent({
  loader: () => import('~/components/BaseAsyncFeed.vue')
})

/**
 * Filter
 */

const [showFilterModal, toggleShowFilterModal] = useToggle()

/**
 * Search
 */

// useFeedComposable()
const { search, uploadDate, videoLength, category, sortBy } = await useSearchFeedComposable()

/**
 * Sort by menu items
 */

const SORTBY_MENU_ITEMS: DropdownMenuItem[] = [
  {
    label: 'Upload date',
    icon: 'i-fa7-solid:clock',
    onSelect: () => {
      sortBy.value = 'Upload date'
    }
  },
  {
    label: 'View count',
    icon: 'i-fa7-solid:eye',
    onSelect: () => {
      sortBy.value = 'View count'
    }
  },
  {
    label: 'Rating',
    icon: 'i-fa7-solid:star',
    onSelect: () => {
      sortBy.value = 'Rating'
    }
  }
]
</script>
