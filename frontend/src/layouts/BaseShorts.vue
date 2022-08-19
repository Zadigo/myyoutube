<template>
  <base-site>
    <template #default>
      <router-view></router-view>
    </template>
  </base-site>
</template>

<script>
import BaseSite from './BaseSite.vue'

export default {
  components: {
    BaseSite
  }
}
    </script>
