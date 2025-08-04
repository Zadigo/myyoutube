<template>
  <VoltDialog v-model:visible="show">
    Share
  </VoltDialog>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })

</script>
