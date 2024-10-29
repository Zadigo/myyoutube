<template>
  <div class="list-group list-group-flush mx-3 mt-4">
    <router-link v-for="navLink in navLinks" :key="navLink.to" :to="{ name: navLink.to }" class="list-group-item list-group-item-action border-0" aria-current="true">
      <font-awesome-icon :icon="navLink.icon" class="me-3" />
      {{ navLink.name }}
    </router-link>

    <hr class="my-4">

    <router-link :to="{ name: 'settings' }" class="list-group-item list-group-item-action border-0" aria-current="true">
      <font-awesome-icon :icon="['fas', 'fa-cog']" class="me-3" />
      Settings
    </router-link>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

const navLinks = [
  {
    name: 'Home',
    to: 'feed',
    icon: 'fas fa-home'
  },
  // {
  //   name: 'Playlists',
  //   to: 'playlists',
  //   icon: 'fas fa-list'
  // },
  // {
  //   name: 'Notifications',
  //   to: 'notifications',
  //   icon: 'fas fa-bell'
  // },
  {
    name: 'My studio',
    to: 'my_studio',
    icon: 'fas fa-chart-simple'
  }
]

export default defineComponent({
  name: 'BaseSidebar',
  setup () {
    return {
      navLinks
    }
  }
})
</script>

<style lang="scss">
$active_color: #1266f1;
$box_shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);

.list-group-item {
  &.active {
    border-radius: 5px;
    box-shadow: $box_shadow;
  }
  
  &.router-link-exact-active {
    z-index: 2;
    color: #fff;
    background-color: $active_color;
    border-color: $active_color;
    border-radius: 5px;
    box-shadow: $box_shadow;
  }
}
</style>
