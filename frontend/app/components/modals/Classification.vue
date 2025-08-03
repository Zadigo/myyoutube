<template>
  <VoltDrawer id="classification-modal" v-model:visible="show" position="right">
    <template #header>
      <h2 class="font-bold text-2xl">
        Classification
      </h2>
    </template>

    <VoltAlert class="my-5">
      Use this tool to signal that this video was not properly
      categorized by the creator and therefore does not correspond to
      the result you were expecting
    </VoltAlert>

    <div class="space-y-2">
      <div>
        <VoltLabel>
          <VoltToggleSwitch />
          <label for="">
            Mark as wrong category
          </label>
        </VoltLabel>
      </div>

      <div>
        <VoltLabel>
          <VoltToggleSwitch />
          <label for="">
            Block this channel
          </label>
        </VoltLabel>
      </div>
    </div>

    <VoltDivider class="my-5" />

    <div class="space-x-2">
      <VoltButton variant="primary">
        <Icon name="i-fa7-solid:check" />
        Save
      </VoltButton>
    </div>
  </VoltDrawer>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })
</script>
