<template>
  <!-- <div class="mx-3 mt-4 flex-col justify-between">
    <div id="links" class="space-y-5">
      <NuxtLink v-for="navLink in navLinks" :key="navLink.to" :to="navLink.to" :aria-current="route.path === navLink.to" class="p-2 px-4 rounded-lg flex gap-3 items-center font-semibold hover:bg-primary-50">
        <font-awesome :icon="navLink.icon" class="me-3" />
        {{ navLink.name }}
      </NuxtLink>
    </div>
  </div> -->
  <SidebarsBase :links="navLinks" />
</template>

<script setup lang="ts">
const navLinks = [
  {
    name: 'Feed',
    to: '/',
    icon: 'i-fa7-solid:home'
  },
  {
    name: 'My account',
    to: '/settings',
    icon: 'i-fa7-solid:user'
  },
  {
    name: 'Algorithm',
    to: '/settings/algorithm',
    icon: 'i-fa7-solid:microchip'
  },
  {
    name: 'Moderation',
    to: '/settings/moderation',
    icon: 'i-fa7-solid:a'
  },
  {
    name: 'Notifications',
    to: '/settings/notifications',
    icon: 'i-fa7-solid:bell'
  },
  {
    name: 'Performance',
    to: '/settings/performance',
    icon: 'i-fa7-solid:tv'
  },
  {
    name: 'Privacy',
    to: '/settings/privacy',
    icon: 'i-fa7-solid:lock'
  },
  {
    name: 'Advanced',
    to: '/settings/advanced',
    icon: 'i-fa7-solid:chart-simple'
  }
]
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
