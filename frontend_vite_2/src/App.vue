<template>
  <v-app>
    <router-view v-slot="{ Component }">
      <transition name="blur">
        <component :is="Component" />
      </transition>
    </router-view>
  </v-app>
</template>

<script lang="ts">
import { useAuthentication } from '@/store/authentication';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
  setup() {
    const store = useAuthentication()
    return {
      store
    }
  },
  created() {
    this.store.loadFromCache()
  }
})
</script>
