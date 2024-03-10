<template>
  <v-app>
    <router-view :key="$route.name"></router-view>
  </v-app>
</template>

<script>
export default {
  name: 'App'
}
</script>


<style scoped>
</style>
