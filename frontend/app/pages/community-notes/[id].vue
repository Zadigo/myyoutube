<template>
  <section id="community-note">
    <div class="grid grid-cols-2">
      <div class="col-span-2 mb-5">
        <nuxt-card>
          <template #content>
            <volt-button to="/community-notes">
              <icon name="i-lucide-arrow-left" />
              Back
            </volt-button>
          </template>
        </nuxt-card>
      </div>

      <!-- User Information -->
      <aside>
        <volt-card>
          <template #content>
            <h1 class="text-2xl font-bold mb-3">Julie Magniola</h1>
            <img src="/avatars/avatar1.png" alt="User Avatar">
          </template>
        </volt-card>
      </aside>

      <!-- Note Details -->
      <div>
        <volt-card>
          <template #content>
            <h2 class="font-bold text-xl">Note Title</h2>
            <p class="text-sm text-gray-600">This is a detailed description of the community note. It provides context and information about the video creator.</p>
          </template> 
        </volt-card>

        <!-- Other Notes -->
        <volt-card class="mt-4">
          <template #content>
            <h2 class="font-bold text-xl mb-4">
              Other Notes on Julie Magniola (36)
            </h2>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              <community-card />
            </div>
          </template>
        </volt-card>
      </div>
    </div>
  </section>
</template>
