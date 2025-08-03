<template>
  <div :class="theme">
    <slot />
  </div>
</template>

<script setup lang="ts">
const { variant = 'neutral' } = defineProps<{ variant?: 'success' | 'error' | 'warning' | 'neutral' }>()

const theme = ref([
  'p-5 rounded-lg mt-5',
  {
    success: 'bg-success-100 text-success-900',
    error: 'bg-error-100 text-error-900',
    warning: 'bg-warning-100 text-warning-900',
    neutral: 'bg-gray-100 text-primary-900'
  }[variant]
])
</script>
