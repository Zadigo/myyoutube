<template>
  <VoltDialog v-model:visible="show" modal>
    <VoltInputText placeholder="Name of your list" flat />
    <VoltInputText placeholder="Search for users..." flat />
    
    <template #footer>
      <VoltButton @click="show=false">
        Cancel
      </VoltButton>

      <VoltButton @click="show=false">
        Save
      </VoltButton>
    </template>
  </VoltDialog>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })
</script>
