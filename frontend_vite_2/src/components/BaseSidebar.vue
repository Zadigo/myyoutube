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
