<template>
  <aside id="previewer" class="border-l-2 border-l-green-100 bg-green-50 dark:bg-green-900 p-5 col-span-3">
    <div v-if="items.length > 0" class="overflow-y-scroll h-137.5 w-full px-2">
      <div ref="infiniteEl">
        <nuxt-card v-for="(item, i) in items" :key="item.id" :data-index="i" class="mb-1">
          <h4 class="font-bold text-1xl">
            {{ item.title }}
          </h4>

          <p class="tex-light text-gray-500 text-sm mb-3">
            {{ item.created_on }}
          </p>

          <p class="font-light">
            {{ item.description }}
          </p>
        </nuxt-card>
      </div>
    </div>

    <div v-else class="text-center text-gray-500 mt-10">
      Feed does not have any items yet.
    </div>
  </aside>
</template>

<script setup lang="ts">
const store = useVideoStore()
const { items } = storeToRefs(store)
</script>
