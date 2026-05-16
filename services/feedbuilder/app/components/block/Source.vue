<template>
  <block-base title="Source" @delete-block="feedsStore.deleteBlock(index)">
    <div class="grid grid-cols-2 gap-1">
      <nuxt-select v-model="data.source" :items="Array.from(sourceNames)" class="w-full" />
      <nuxt-select v-model="data.duration" :items="Array.from(duration)" class="w-full" />
    </div>
  </block-base>
</template>

<script setup lang="ts">
import type { SourceOptions } from '~/types'

const emit = defineEmits<{ 'update:modelValue': [value: SourceOptions] }>()
const props = defineProps<{ modelValue: SourceOptions, index: number }>()

const data = useVModel(props, 'modelValue', emit, {
  passive: true,
  eventName: 'update:modelValue'
})

const feedsStore = useFeedsStore()
</script>
