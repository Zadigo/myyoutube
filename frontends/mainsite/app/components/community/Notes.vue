<template>
  <section id="notes">
    <u-card class="shadow-sm mt-4">
      <h2 class="font-bold text-xl mb-4">
        Recent Notes
      </h2>

      <p class="font-light mb-4">
        Here are some of the most recent community notes that have been added. You can view more details by clicking on each note.
      </p>

      <u-separator class="mb-4" />

      <!-- Actions -->
      <div class="flex justify-between gap-2 items-center">
        <u-input-text placeholder="Search" v-model="search" />

        <div class="space-x-2">
          <u-button variant="subtle" class="mb-4">
            <icon name="lucide:filter" />
            Filter Notes
          </u-button>

          <u-button variant="subtle" class="mb-4">
            <icon name="lucide:plus" />
            Add a Note
          </u-button>
        </div>
      </div>

      <!-- Notes -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <community-card v-for="note in searchedCommunityNotes" :key="note.node.id" :note="note" />
      </div>
    </u-card>
  </section>
</template>

<script setup lang="ts">
/**
 * Get Notes
 */

const { search, searchedCommunityNotes } = await useCommunityNotesComposable()
</script>
