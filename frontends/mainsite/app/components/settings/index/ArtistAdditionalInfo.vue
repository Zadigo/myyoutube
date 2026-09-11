<template>
  <div v-if="isArtist" id="professional" class="space-x-1 p-2 rounded-lg bg-secondary-50">
    <u-input placeholder="Artist name" />
    <u-input placeholder="Spotify ID" />
    <u-input placeholder="Spotify profile" />
  </div>
</template>

<script setup lang="ts">
const settingsStore = useSettingsStore()
const { isArtist } = storeToRefs(settingsStore)
</script>
