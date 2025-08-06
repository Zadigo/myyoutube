<template>
  <BlockBase title="Limit" @delete-block="handleDeleteBlock(index)">
    <div class="row">
      <div class="col-12">
        <div class="d-flex gap-2">
          <BaseInput v-model="limit" :min="0" variant="solo-filled" hide-details flat @change="emit('define-options', limit)" />
        </div>
      </div>
    </div>
  </BlockBase>
</template>

<script setup lang="ts">
const { handleDeleteBlock } = useBlocks()
const limit = ref<number>(100)

defineProps({
  index: {
    type: Number,
    required: true
  }
})

const emit = defineEmits({
  'define-options' (_limit: number) {
    return true
  }
})
</script>
