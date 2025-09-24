<template>
  <sidebars-base :links="navLinks">
    <template #footer>
      <volt-divider class="my-4" />

      {{ isAuthenticated }}

      <nuxt-link to="/settings" class="p-2 px-4 bg-primary-200 dark:bg-primary-800 rounded-lg flex gap-3 items-center text-surface-50 dark:text-surface-50 font-semibold" aria-current="true">
        <icon name="i-lucide-settings" />
        Settings
      </nuxt-link>
    </template>
  </sidebars-base>
</template>

<script setup lang="ts">
const navLinks = [
  {
    name: 'Home',
    to: '/',
    icon: 'i-lucide-home'
  },
  {
    name: 'Playlists',
    to: '/playlists',
    icon: 'i-lucide-list'
  },
  {
    name: 'Notifications',
    to: '/notifications',
    icon: 'i-lucide-bell'
  },
  {
    name: 'Community notes',
    to: '/community-notes',
    icon: 'i-lucide-book-open-check'
  },
  {
    name: 'My studio',
    to: '/studio',
    icon: 'i-lucide-chart-area'
  }
]

const isAuthenticated = useState('isAuthenticated')
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
