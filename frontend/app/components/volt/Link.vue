<template>
  <NuxtLinkLocale :to="to" :class="theme">
    <slot />
  </NuxtLinkLocale>
</template>

<script lang="ts" setup>
defineProps<{
  to: string
}>()

const theme = ref([
  `bg-primary hover:bg-primary-emphasis active:bg-primary-emphasis-alt text-primary-contrast 
  px-3 py-2 gap-2 rounded-md font-medium focus-visible:outline focus-visible:outline-offset-2 
  focus-visible:outline-primary`
])
</script>
