<template>
  <section id="community-notes" class="mx-auto">
    <VoltCard class="shadow-sm">
      <template #content>
        <h1 class="font-bold text-2xl mb-4">
          Community Notes
        </h1>

        <p class="font-light">
          Community notes are peer reviewed notes redacted by the community to provide additional context and information about the creators of videos on YouTube. 
          They can help viewers understand the content better, correct misinformation, or provide useful insights that enhance the viewing experience.
        </p>

        <VoltButton variant="text" class="mt-3">
          <Icon name="i-fa7-solid:arrow-up-right-from-square" class="me-2" />
          Learn more
        </VoltButton>
      </template>
    </VoltCard>

    <slot />
  </section>
</template>

<script setup lang="ts">
// TODO: Create a specific dashboard for community notes
</script>
