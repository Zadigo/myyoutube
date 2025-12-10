<template>
  <nav class="bg-slate-50 dark:bg-primary dark:text-surface-50 fixed top-0 left-0 right-0 p-2 border-b border-slate-50 dark:border-slate-500 z-40">
    <div class="flex items-center ps-[calc(240px+1rem)] space-x-2">
      <VoltButton class="navbar-toggler" variant="outlined" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation" @click="() => { toggle() }">
        <Icon name="i-fa7-solid:bars" />
      </VoltButton>

      <NuxtLink to="/" class="uppercase font-bold">
        My Youtube
      </NuxtLink>

      <ul class="ms-auto">
        <VoltAvatar image="/avatars/avatar1.png" shape="circle" size="normal" />
      </ul>
    </div>
  </nav>
</template>

<script setup lang="ts">
/**
 * Sidebar
 */

const showSidebar = useState<boolean>('showSidebar')
const toggle = useToggle(showSidebar)
</script>
