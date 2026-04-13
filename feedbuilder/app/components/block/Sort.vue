<template>
  <block-base title="Some title" @delete-block="feedsStore.deleteBlock(index)">
    <div class="grid grid-cols-2 gap-4">
      <nuxt-select v-model="sort.by" :items="Array.from(sortBy)" />
      <nuxt-select v-model="sort.direction" :items="Array.from(sortDirection)" />
    </div>
  </block-base>
</template>

<script setup lang="ts">
import type { SortOptions } from '~/types'

const feedsStore = useFeedsStore()

const props = defineProps<{ modelValue: SortOptions, index: number }>()
const emit = defineEmits<{ 'update:modelValue': [value: SortOptions] }>()

const sort = useVModel(props, 'modelValue', emit, {
  passive: true,
  eventName: 'update:modelValue'
})
</script>
