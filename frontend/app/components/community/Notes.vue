<template>
  <section id="notes">
    <volt-card class="shadow-sm mt-4">
      <template #content>
        <h2 class="font-bold text-xl mb-4">
          Recent Notes
        </h2>

        <p class="font-light mb-4">
          Here are some of the most recent community notes that have been added. You can view more details by clicking on each note.
        </p>

        <volt-divider class="mb-4" />

        <div class="flex justify-between gap-2 items-center">
          <volt-input-text placeholder="Search" />

          <div class="space-x-2">
            <volt-secondary-button variant="secondary" class="mb-4">
              <Icon name="i-fa7-solid:filter" class="me-2" />
              Filter Notes
            </volt-secondary-button>

            <volt-secondary-button variant="primary" class="mb-4">
              <Icon name="i-fa7-solid:plus" class="me-2" />
              Add a Note
            </volt-secondary-button>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <community-card />
        </div>
      </template>
    </volt-card>
  </section>
</template>
