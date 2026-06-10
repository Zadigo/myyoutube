<template>
  <div v-if="isBusiness" id="professional" class="space-x-1 p-2 rounded-lg bg-secondary-50">
    <VoltInputText placeholder="Business ID" />
    <VoltInputText placeholder="Business VAT" />
  </div>
</template>

<script setup lang="ts">
const settingsStore = useSettingsStore()
const { isBusiness } = storeToRefs(settingsStore)
</script>
