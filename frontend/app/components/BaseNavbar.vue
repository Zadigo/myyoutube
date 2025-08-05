<template>
  <nav class="bg-white fixed top-0 left-0 right-0 p-2 border-b border-slate-50 z-20">
    <div class="flex items-center ps-[calc(240px+1rem)] space-x-2">
      <VoltButton class="navbar-toggler" variant="outlined" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation" @click="() => emit('show:navbar', true)">
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
const emit = defineEmits<{ 'show:navbar': [boolean] }>()
</script>
