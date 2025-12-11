<template>
  <volt-dialog v-model:visible="showShareModal">
    Share
  </volt-dialog>
</template>

<script setup lang="ts">
/**
 * Modal
 */

const { showShareModal } = tryUseVideoDetailModalsStore()
</script>
