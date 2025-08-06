<template>
  <BlockBase title="Limit" @delete-block="feedsStore.deleteBlock(index)">
    <VoltInputText v-model="limit" :min="0" class="w-full" />
  </BlockBase>
</template>

<script setup lang="ts">
const feedsStore = useFeedsStore()

const props = defineProps<{ modelValue: number, index: number }>()
const emit = defineEmits<{ 'update:modelValue': [limit: number] }>()

const limit = useVModel(props, 'modelValue', emit, {
  passive: true,
  eventName: 'update:modelValue'
})
</script>
