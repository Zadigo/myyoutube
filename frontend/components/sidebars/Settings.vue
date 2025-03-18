<template>
  <div class="list-group list-group-flush mx-3 mt-4">
    <NuxtLink v-for="navLink in navLinks" :key="navLink.to" :to="navLink.to" :aria-current="route.path === navLink.to" class="list-group-item list-group-item-action border-0">
      <font-awesome :icon="navLink.icon" class="me-3" />
      {{ navLink.name }}
    </NuxtLink>
  </div>
</template>

<script setup lang="ts">
const navLinks = [
  {
    name: 'Feed',
    to: '/',
    icon: 'fas fa-home'
  },
  {
    name: 'My account',
    to: '/settings',
    icon: 'fas fa-user'
  },
  {
    name: 'Algorithm',
    to: '/settings/algorithm',
    icon: 'fas fa-microchip'
  },
  {
    name: 'Moderation',
    to: '/settings/moderation',
    icon: 'fas fa-a'
  },
  {
    name: 'Notifications',
    to: '/settings/notifications',
    icon: 'fas fa-bell'
  },
  {
    name: 'Performance',
    to: '/settings/performance',
    icon: 'fas fa-tv'
  },
  {
    name: 'Privacy',
    to: '/settings/privacy',
    icon: 'fas fa-lock'
  },
  {
    name: 'Advanced',
    to: '/settings/advanced',
    icon: 'fas fa-chart-simple'
  }
]

const route = useRoute()
</script>

<style lang="scss" scoped>
$active_color: #1266f1;
$box_shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);

.list-group-item {
  &.active {
    border-radius: 5px;
    box-shadow: $box_shadow;
  }

  &[class*="-exact-active"] {
    z-index: 2;
    color: #fff;
    background-color: $active_color;
    border-color: $active_color;
    border-radius: 5px;
    box-shadow: $box_shadow;
  }
}
</style>
