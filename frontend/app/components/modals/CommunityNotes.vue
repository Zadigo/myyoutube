<template>
  <VoltDialog id="notes" v-model:visible="show">
    Some text
  </VoltDialog>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })
</script>
