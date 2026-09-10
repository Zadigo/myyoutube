<template>
  <u-modal v-model:open="showShareModal">
    Share
  </u-modal>
</template>

<script setup lang="ts">
/**
 * Modal
 */

const { showShareModal } = tryUseVideoDetailModalsStore()
</script>
