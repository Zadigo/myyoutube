<template>
  <nuxt-layout>
    <nuxt-loading-indicator />
    <nuxt-page />
  </nuxt-layout>
</template>

<script setup lang="ts">
useNuxtAuthentication()
useSession()

/**
 * Sidebar
 */

useState<boolean>('showSidebar', () => false)

/**
 * Background
 */

const tokens = ['bg-primary-50', 'dark:bg-primary-900', 'dark:text-surface-50']

onMounted(() => {
  document.body.classList.add(...tokens)
})

onUnmounted(() => {
  document.body.classList.remove(...tokens)
})
</script>
