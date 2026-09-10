<template>
  <u-modal v-model:open="show" modal>
    <template #body>
      <u-input placeholder="Name of your list" flat />
      <u-input placeholder="Search for users..." flat />
    </template>

    <template #footer>
      <u-button @click="show = false">
        Cancel
      </u-button>

      <u-button @click="show = false">
        Save
      </u-button>
    </template>
  </u-modal>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })
</script>
