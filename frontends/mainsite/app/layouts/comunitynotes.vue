<template>
  <section id="community-notes" class="mx-auto">
    <u-card class="shadow-sm">
      <template #content>
        <h1 class="font-bold text-2xl mb-4">
          Community Notes
        </h1>

        <p class="font-light">
          Community notes are peer reviewed notes redacted by the community to provide additional context and information about the creators of videos on YouTube. 
          They can help viewers understand the content better, correct misinformation, or provide useful insights that enhance the viewing experience.
        </p>

        <u-button variant="soft" class="mt-3">
          <Icon name="i-fa7-solid:arrow-up-right-from-square" class="me-2" />
          Learn more
        </u-button>
      </template>
    </u-card>

    <slot />
  </section>
</template>

<script setup lang="ts">
// TODO: Create a specific dashboard for community notes
</script>
