<template>
  <VoltDialog v-model:visible="show">
    <VoltInputText type="number" :min="10" :max="500" :step="10" variant="outlined" />
  </VoltDialog>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })
</script>
