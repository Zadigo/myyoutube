<template>
  <section :class="{ full: !showSidebar }" class="relative">
    <header>
      <!-- Sidebar -->
      <Transition name="sidebar" mode="out-in">
        <SidebarsSite v-if="showSidebar" />
      </Transition>

      <!-- Navbar -->
      <BaseNavbar @show:navbar="() => toggle()" />
    </header>

    <main class="mt-[calc(55px+1rem)] mb-10 ps-[calc(240px+1rem)] pe-2">
      <slot />
    </main>
  </section>
</template>

<script setup lang="ts">
import { useSidebar } from '~/composables/use'

const { showSidebar, toggle } = useSidebar()
</script>
