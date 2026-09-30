<template>
  <u-modal v-model:open="showShareModal">
    <template #body>
      Share
    </template>
  </u-modal>
</template>

<script setup lang="ts">
/**
 * Modal
 */

const { showShareModal } = useVideoDetailModalsStore()
</script>
