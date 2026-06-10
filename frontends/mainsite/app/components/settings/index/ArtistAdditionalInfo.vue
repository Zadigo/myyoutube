<template>
  <div v-if="isArtist" id="professional" class="space-x-1 p-2 rounded-lg bg-secondary-50">
    <VoltInputText placeholder="Artist name" />
    <VoltInputText placeholder="Spotify ID" />
    <VoltInputText placeholder="Spotify profile" />
  </div>
</template>

<script setup lang="ts">
const settingsStore = useSettingsStore()
const { isArtist } = storeToRefs(settingsStore)
</script>
