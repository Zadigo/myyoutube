<template>
  <u-modal id="notes" v-model:open="show">
    <template #body>
      Some text
    </template>
  </u-modal>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })
</script>
