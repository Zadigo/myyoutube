<template>
  <div class="mx-3 mt-4 spae-y-2">
    <NuxtLink v-for="navLink in navLinks" :key="navLink.to" :to="navLink.to" :aria-current="route.path === navLink.to" class="p-2 rounded-lg flex gap-1 items-center font-semibold">
      <Icon :name="navLink.icon" class="me-3" />
      {{ navLink.name }}
    </NuxtLink>

    <VoltDivider class="my-4" />

    <NuxtLink to="/settings" class="p-2 bg-primary-500 rounded-lg flex gap-1 items-center text-white font-semibold" aria-current="true">
      <Icon name="i-fa7-solid:cog" class="me-3" />
      Settings
    </NuxtLink>
  </div>
</template>

<script setup>
const navLinks = [
  {
    name: 'Home',
    to: '/',
    icon: 'i-fa7-solid:home'
  },
  {
    name: 'Playlists',
    to: '/playlists',
    icon: 'i-fa7-solid:list'
  },
  {
    name: 'Notifications',
    to: '/notifications',
    icon: 'i-fa7-solid:bell'
  },
  {
    name: 'My studio',
    to: '/studio',
    icon: 'i-fa7-solid:chart-simple'
  }
]

const route = useRoute()
</script>

<style lang="scss" scoped>
$box_shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);

a {
  &.active {
    border-radius: 5px;
    box-shadow: $box_shadow;
  }
  
  &[class*="-exact-active"] {
    z-index: 2;
    color: var(--p-surface-0);
    background-color: var(--p-primary-500);
    border-color: var(--p-primary-500);
    border-radius: 5px;
    box-shadow: $box_shadow;
  }
}
</style>
