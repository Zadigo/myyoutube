<template>
  <router-view :key="$route.name"></router-view>
</template>

<script>
import { provide } from 'vue'

export default {
  name: 'App',
  setup () {
    provide('darkMode', false)
  }
}
</script>
