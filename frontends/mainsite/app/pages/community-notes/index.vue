<template>
  <section id="community-notes" class="mx-auto">
    <u-card class="shadow-sm">
      <h1 class="font-bold text-2xl mb-4">
        Community Notes
      </h1>

      <p class="font-light">
        Community notes are peer reviewed notes redacted by the community to provide additional context and information about the creators of videos on YouTube. 
        They can help viewers understand the content better, correct misinformation, or provide useful insights that enhance the viewing experience.
      </p>

      <u-button variant="ghost" class="mt-3">
        <icon name="lucide:external-link" />
        Learn more
      </u-button>
    </u-card>

    <suspense>
      <template #default>
        <async-community-notes />
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
const AsyncCommunityNotes = defineAsyncComponent({
  loader: async () => import('~/components/community/Notes.vue'),
  suspensible: true,
  delay: 200,
  timeout: 10000
})
</script>
