<template>
  <u-slideover v-model:open="show" modal>
    <u-input placeholder="Name of your list" flat />
    <u-input placeholder="Search for users..." flat />
    
    <template #footer>
      <u-button @click="show=false">
        Cancel
      </u-button>

      <u-button @click="show=false">
        Save
      </u-button>
    </template>
  </u-slideover>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })
</script>
