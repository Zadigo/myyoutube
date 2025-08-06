<template>
  <BlockBase @delete-block="feedsStore.deleteBlock(index)">
    <div class="grid grid-cols-2 gap-4">
      <VoltSelect v-model="data.by" :options="sortBy" />
      <VoltSelect v-model="data.direction" :options="sortDirection" />
    </div>
  </BlockBase>
</template>

<script setup lang="ts">
import { sortBy, sortDirection } from '~/data'
import type { SortOptions } from '~/types'

const feedsStore = useFeedsStore()

const emit = defineEmits<{ 'update:modelValue': [value: SortOptions] }>()
const props = defineProps<{ modelValue: SortOptions, index: number }>()

const data = useVModel(props, 'modelValue', emit, {
  passive: true,
  eventName: 'update:modelValue'
})
</script>
