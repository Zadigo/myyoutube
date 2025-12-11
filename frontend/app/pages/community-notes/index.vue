<template>
  <section id="community-notes" class="mx-auto">
    <volt-card class="shadow-sm">
      <template #content>
        <h1 class="font-bold text-2xl mb-4">
          Community Notes
        </h1>

        <p class="font-light">
          Community notes are peer reviewed notes redacted by the community to provide additional context and information about the creators of videos on YouTube. 
          They can help viewers understand the content better, correct misinformation, or provide useful insights that enhance the viewing experience.
        </p>

        <volt-button variant="text" class="mt-3">
          <icon name="lucide:external-link" />
          Learn more
        </volt-button>
      </template>
    </volt-card>

    <suspense>
      <template #default>
        <community-notes />
      </template>

      <template #fallback>
        <div class="text-center my-4">
          Loading...
        </div>
      </template>
    </suspense>
  </section>
</template>

<script setup lang="ts">
</script>
