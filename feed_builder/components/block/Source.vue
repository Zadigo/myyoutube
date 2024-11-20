<template>
  <BlockBase @delete-block="handleDeleteBlock">
    <div class="row">
      <div class="col-6">
        <v-select v-model="selectedOptions.source" :items="sourceNames" variant="solo-filled" hide-details flat @change="emit('define-source', selectedOptions)" />
      </div>
      
      <div class="col-6">
        <v-select v-model="selectedOptions.duration" :items="duration" variant="solo-filled" hide-details flat @change="emit('define-source', selectedOptions)" />
      </div>
    </div>
  </BlockBase>
</template>

<script lang="ts" setup>
interface SourceOptions {
  duration: '30 minutes' | '3 hours' | '12 hours' | '24 hours' | '3 days' | '7 days '
  source: 'Entire network' | 'Tags' | 'Single user' | 'List' | 'Feed' | 'Single post' | 'Labels'
}

const duration = [
  '30 minutes',
  '3 hours',
  '12 hours',
  '24 hours',
  '3 days',
  '7 days'
]

const sourceNames = [
  'Entire network',
  'Tags',
  'Single user',
  'List',
  'Feed',
  'Single post',
  'Labels'
]

const selectedOptions = ref<SourceOptions>({
  duration: '24 hours',
  source: 'Entire network'
})

const emit = defineEmits({
  'define-source' (_data: SourceOptions) {
    return true
  },
  'delete-block' (_index: number) {
    return true
  }
})

const props = defineProps({
  index: {
    type: Number,
    required: true
  }
})

function handleDeleteBlock () {
  emit('delete-block', props.index)
}
</script>>
