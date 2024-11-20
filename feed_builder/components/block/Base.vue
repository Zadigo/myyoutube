<template>
  <div class="card shadow-sm">
    <div class="card-header border-bottom-0 d-flex justify-content-between align-items-center">
      <v-btn variant="text" draggable="true">
        <font-awesome icon="grip-vertical" />
      </v-btn>

      <v-btn variant="tonal" @click="handleDeleteBlock">
        <font-awesome icon="trash" />
      </v-btn>
    </div>
    
    <div class="card-body">
      <div class="row">
        <slot />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const emit = defineEmits({
  'delete-block' () {
    return true
  }
})

function handleDeleteBlock () {
  emit('delete-block')
}
</script>
