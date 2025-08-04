<template>
  <div class="space-y-3 flex-col my-4">
    <div :class="theme">
      <slot name="description" />

      <div v-if="help" class="mt-2">
        <VoltButton to="help" variant="text" color="primary">
          <Icon name="i-fa7-solid:arrow-up-right-from-square" class="me-1" />
          Learn more
        </VoltButton>
      </div>
    </div>

    <slot />
  </div>
</template>

<script lang="ts" setup>
const props = defineProps<{
  help?: string
  callout?: boolean
}>()

const theme = ref<(string | Record<string, string | boolean | undefined>)[]>([
  'font-light',
  {
    'bg-slate-200 p-5 rounded-lg': props.callout
  }
])
</script>
