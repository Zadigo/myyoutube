<template>
  <BlockBase title="Source" @delete-block="feedsStore.deleteBlock(index)">
    <div class="grid grid-cols-2 gap-1">
      <VoltSelect v-model="data.source" :options="sourceNames" class="w-full" />
      <VoltSelect v-model="data.duration" :options="duration" class="w-full" />
    </div>
  </BlockBase>
</template>

<script setup lang="ts">
import type { SourceOptions } from '~/types'
import { duration, sourceNames } from '~/data'

const emit = defineEmits<{ 'update:modelValue': [value: SourceOptions] }>()
const props = defineProps<{ modelValue: SourceOptions, index: number }>()

const data = useVModel(props, 'modelValue', emit, {
  passive: true,
  eventName: 'update:modelValue'
})

const feedsStore = useFeedsStore()
</script>
