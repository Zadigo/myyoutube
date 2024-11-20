<template>
  <BlockBase @delete-block="handleDeleteBlock(index)">
    <div class="row">
      <div class="col-6">
        <v-select v-model="sortSelection.sort_by" :items="sortBy" variant="solo-filled" hide-details flat @change="emit('define-options', sortSelection)" />
      </div>
      
      <div class="col-6">
        <v-select v-model="sortSelection.direction" :items="['Ascending', 'Descending']" variant="solo-filled" hide-details flat @change="emit('define-options', sortSelection)" />
      </div>
    </div>
  </BlockBase>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

type SortBy = 'Creation date' | 'Like count' | 'Reply count' | 'Random'
interface SortOptions {
  sort_by: SortBy
  direction: 'Ascending' | 'Descending'
}

const sortBy = [
  'Creation date',
  'Like count',
  'Reply count',
  'Random'
]

const { handleDeleteBlock } = useBlocks()

const emit = defineEmits({
  'define-options' (_data: SortOptions) {
    return true
  }
})

defineProps({
  index: {
    type: Number,
    required: true
  }
})

const sortSelection = ref<SortOptions>({
  sort_by: 'Creation date',
  direction: 'Ascending'
})
</script>
