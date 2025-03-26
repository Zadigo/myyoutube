<template>
  <BlockBase title="Source" @delete-block="handleDeleteBlock">
    <div class="row">
      <div class="p-1">
        <v-select v-model="data.source" :items="sourceNames" variant="solo-filled" hide-details flat />
      </div>
      
      <div class="p-1">
        <v-select v-model="data.duration" :items="duration" variant="solo-filled" hide-details flat />
      </div>
    </div>
  </BlockBase>
</template>

<script setup lang="ts">
import type { SourceOptions } from '~/types'
import { duration, sourceNames } from '~/data'

const emit = defineEmits({
  'update:modelValue'(_value: SourceOptions) {
    return true
  },
  'update-data'() {
    return true
  },
  'delete-block' (_index: number) {
    return true
  }
})

const props = defineProps({
  modelValue: {
    type: Object as PropType<SourceOptions>,
    required: true
  },
  index: {
    type: Number,
    required: true
  }
})

const data = computed({
  get: () => props.modelValue,
  set(value: SourceOptions) {
    emit('update:modelValue', value)
    emit('update-data')
  }
})

function handleDeleteBlock () {
  emit('delete-block', props.index)
}
</script>>
