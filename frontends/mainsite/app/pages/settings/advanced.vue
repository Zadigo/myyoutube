<template>
  <section id="algorithm">
    <settings-card class="shadow-sm" title="Advanced" subtitle="Manage what you share on YouTube">
      <volt-input-otp :length="4" />
    </settings-card>
  </section>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'settings'
})
</script>
