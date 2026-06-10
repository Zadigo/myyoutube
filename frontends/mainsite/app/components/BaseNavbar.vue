<template>
  <nav class="fixed top-0 left-0 h-(--navbar-height) w-full px-6 md:px-16 lg:px-24 xl:px-32 flex items-center justify-between z-30 bg-white dark:bg-primary-950 dark:text-primary-50 transition-all">
  <!-- <nav class="bg-slate-50 dark:bg-primary dark:text-surface-50 fixed top-0 left-0 right-0 p-2 border-b border-slate-50 dark:border-slate-500 z-40"> -->
    <div :class="theme" class="flex items-center space-x-2 transition-all ease-in-out">
      <volt-button class="navbar-toggler" variant="outlined" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation" @click="() => { toggle() }">
        <icon name="i-fa7-solid:bars" />
      </volt-button>

      <nuxt-link-locale to="/" class="uppercase font-bold">
        My Youtube
      </nuxt-link-locale>
    </div>

    <ul class="ms-auto">
      <volt-button @click="() => { toggleDarkMode() }">Dark</volt-button>
      <volt-avatar image="/avatars/avatar1.png" shape="circle" size="normal" />
    </ul>
  </nav>
</template>

<script setup lang="ts">
/**
 * Sidebar
 */

const showSidebar = useState<boolean>('showSidebar')
const toggle = useToggle(showSidebar)

const theme = computed(() => {
  return {
    'ps-[calc(var(--sidebar-width)+1rem)]': showSidebar.value,
    'ps-0': !showSidebar.value
  }
})

/**
 * Darkmode
 */

const { toggleDarkMode } = useDarkModeComposable()
</script>
