<template>
  <section :class="{ full: !showSidebar }" class="relative">
    <header>
      <!-- Sidebar -->
      <transition mode="out-in" enter-active-class="duration-500" leave-active-class="duration-400" enter-from-class="-translate-x-(--sidebar-width)" enter-to-class="translate-x-0" leave-from-class="opacity-100 translate-x-0" leave-to-class="opacity-0 -translate-x-(--sidebar-width)">
        <sidebars-site v-if="showSidebar" />
      </transition>

      <!-- Navbar -->
      <base-navbar @show:navbar="() => toggle()" />
    </header>

    <main :class="theme" class="mt-[calc(55px+1rem)] mb-10 z-20 transition-all ease-in-out duration-600">
      <slot />
    </main>
  </section>
</template>

<script setup lang="ts">
const showSidebar = useState<boolean>('showSidebar')
const toggle = useToggle(showSidebar)

const theme = computed(() => {  
  return [
    {
      'px-10': !showSidebar.value,
      'ps-[calc(var(--sidebar-width)+1rem)] pe-3': showSidebar.value,
    }
  ]
})
</script>
