<template>
  <BlockBase @delete-block="handleDeleteBlock(index)">
    <div class="row">
      <div class="col-12">
        <div class="d-flex gap-2">
          <v-text-field v-model="limit" :min="0" variant="solo-filled" hide-details flat @change="emit('define-option', limit)" />
        </div>
      </div>
    </div>
  </BlockBase>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const { handleDeleteBlock } = useBlocks()
const limit = ref<number>(100)

defineProps({
    index: {
        type: Number,
        required: true
    }
})

const emit = defineEmits({
  'define-option' (_limit: number) {
    return true
  }
})
</script>
