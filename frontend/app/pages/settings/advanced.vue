<template>
  <section id="algorithm">
    <SettingsCard class="shadow-sm" title="Advanced" subtitle="Manage what you share on YouTube">
      <VoltInputOtp :length="4" />
    </SettingsCard>
  </section>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'settings'
})
</script>
