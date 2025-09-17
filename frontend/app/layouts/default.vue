<template>
  <section :class="{ full: !showSidebar }" class="relative">
    <header>
      <!-- Sidebar -->
      <transition name="sidebar" mode="out-in">
        <SidebarsSite v-if="showSidebar" />
      </transition>

      <!-- Navbar -->
      <BaseNavbar @show:navbar="() => toggle()" />
    </header>

    <main class="mt-[calc(55px+1rem)] mb-10 ps-[calc(var(--sidebar-width)+1rem)] pe-2">
      <slot />
    </main>
  </section>
</template>

<script setup lang="ts">
import { useSidebar } from '~/composables/use'

const { showSidebar, toggle } = useSidebar()
</script>
