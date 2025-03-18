<template>
  <div class="list-group list-group-flush mx-3 mt-4">
    <NuxtLink v-for="navLink in navLinks" :key="navLink.to" :to="navLink.to" :class="listGroupItemClasses" :aria-current="route.path === navLink.to" class="list-group-item list-group-item-action border-0">
      <font-awesome :icon="navLink.icon" class="me-3" />
      {{ navLink.name }}
    </NuxtLink>

    <hr class="my-4">

    <NuxtLink to="/settings" class="list-group-item list-group-item-action border-0" aria-current="true">
      <font-awesome icon="cog" class="me-3" />
      Settings
    </NuxtLink>
  </div>
</template>

<script setup>
const navLinks = [
  {
    name: 'Home',
    to: '/',
    icon: 'home'
  },
  {
    name: 'Playlists',
    to: '/playlists',
    icon: 'fas fa-list'
  },
  {
    name: 'Notifications',
    to: '/notifications',
    icon: 'fas fa-bell'
  },
  {
    name: 'My studio',
    to: '/studio',
    icon: 'chart-simple'
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
