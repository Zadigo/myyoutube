<template>
  <BlockBase @delete-block="feedsStore.deleteBlock(index)">
    <div class="grid grid-cols-2 gap-4">
      <VoltSelect v-model="sort.by" :options="sortBy" />
      <VoltSelect v-model="sort.direction" :options="sortDirection" />
    </div>
  </BlockBase>
</template>

<script setup lang="ts">
import { sortBy, sortDirection } from '~/data'
import type { SortOptions } from '~/types'

const feedsStore = useFeedsStore()

const props = defineProps<{ modelValue: SortOptions, index: number }>()
const emit = defineEmits<{ 'update:modelValue': [value: SortOptions] }>()

const sort = useVModel(props, 'modelValue', emit, {
  passive: true,
  eventName: 'update:modelValue'
})
</script>
