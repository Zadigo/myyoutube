<template>
  <BlockBase title="Limit" @delete-block="feedsStore.deleteBlock(index)">
    <VoltInputText v-model="data.limit" :min="0" class="w-full" />
  </BlockBase>
</template>

<script setup lang="ts">
import type { LimitOptions } from '~/types'

const feedsStore = useFeedsStore()

const props = defineProps<{ modelValue: LimitOptions, index: number }>()
const emit = defineEmits<{ 'update:modelValue': [limit: LimitOptions] }>()

const data = useVModel(props, 'modelValue', emit, {
  passive: true,
  eventName: 'update:modelValue'
})
</script>
