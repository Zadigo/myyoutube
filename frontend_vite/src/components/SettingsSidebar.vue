<template>
  <div class="list-group list-group-flush mx-3 mt-4">
    <router-link v-for="navLink in navLinks" :key="navLink.to" :to="{ name: navLink.to }" class="list-group-item list-group-item-action border-0" aria-current="true">
      <font-awesome-icon :icon="navLink.icon" class="me-3" />
      {{ navLink.name }}
    </router-link>
  </div>
</template>

<script>
const navLinks = [
  {
    name: 'Feed',
    to: 'feed',
    icon: 'fas fa-home'
  },
  {
    name: 'My account',
    to: 'settings',
    icon: 'fas fa-user'
  },
  {
    name: 'Algorithm',
    to: 'settings_algorithm',
    icon: 'fas fa-a'
  },
  {
    name: 'Notifications',
    to: 'settings_notifications',
    icon: 'fas fa-bell'
  },
  {
    name: 'Performance',
    to: 'settings_performance',
    icon: 'fas fa-tv'
  },
  {
    name: 'Privacy',
    to: 'settings_privacy',
    icon: 'fas fa-lock'
  },
  {
    name: 'Advanced',
    to: 'settings_advanced',
    icon: 'fas fa-chart-simple'
  }
]
export default {
  name: 'SettingsSidebar',
  setup () {
    return {
      navLinks
    }
  }
}
</script>
