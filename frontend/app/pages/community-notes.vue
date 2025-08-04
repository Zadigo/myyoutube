<script setup lang="ts">
import { VoltSecondaryButton } from '#components';

</script>

<template>
  <section id="community-notes" class="container mx-auto px-4">
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

    <section id="notes">
      <VoltCard class="shadow-sm mt-4">
        <template #content>
          <h2 class="font-bold text-xl mb-4">
            Recent Notes
          </h2>

          <p class="font-light mb-4">
            Here are some of the most recent community notes that have been added. You can view more details by clicking on each note.
          </p>

          <VoltDivider class="mb-4" />

          <div class="flex justify-between gap-2 items-center">
            <VoltInputText placeholder="Search" />
            
            <div class="space-x-2">
              <VoltSecondaryButton variant="secondary" class="mb-4">
                <Icon name="i-fa7-solid:filter" class="me-2" />
                Filter Notes
              </VoltSecondaryButton>

              <VoltSecondaryButton variant="primary" class="mb-4">
                <Icon name="i-fa7-solid:plus" class="me-2" />
                Add a Note
              </VoltSecondaryButton>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <!-- Example Note Card -->
            <VoltCard class="shadow-sm">
              <template #content>
                <h3 class="font-semibold text-lg">Note Title</h3>
                <p class="text-sm text-gray-600">This is a brief description of the note. It provides context and information about the video creator.</p>
                <VoltButton size="small" variant="primary" class="mt-2">View Note</VoltButton>
              </template>
            </VoltCard>
            <!-- Repeat for more notes -->
          </div>
        </template>
      </VoltCard>
    </section>
  </section>
</template>
