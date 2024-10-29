<template>
  <section :class="{ full: !showSidebar }" class="dashboard">
    <header>
      <!-- Sidebar -->
      <transition tag="div" name="sidebar" mode="out-in">
        <nav v-if="showSidebar" id="sidebar" class="collapse d-lg-block sidebar collapse bg-white">
          <div class="position-sticky">
            <settings-sidebar v-if="$route.meta.requiresSettingsNav" />
            <base-sidebar v-else />
          </div>
        </nav>
      </transition>

      <!-- Navbar -->
      <nav v-show="$route.meta.requiresNav" id="main-navbar" class="navbar navbar-expand-lg fixed-top navbar-light bg-white">
        <div class="container-fluid">
          <button class="navbar-toggler" type="button" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
            <font-awesome-icon icon="bars" />
          </button>
          
          <v-btn rounded="xl" text flat @click="showSidebar = !showSidebar">
            <font-awesome-icon :icon="[ 'fas', 'fa-bar' ]" />
          </v-btn>

          <router-link :to="{ name: 'feed' }" class="navbar-brand">
            My Youtube
          </router-link>

          <!-- <form @submit.prevent>
            <v-text-field outlined></v-text-field>
          </form> -->

          <ul class="navbar-nav ms-auto d-flex flex-row">
            <v-avatar image="/avatar1.png" size="35" />
          </ul>
        </div>
      </nav>
    </header>

    <main>
      <div class="container pt-4">
        <router-view />
      </div>
    </main>
  </section>
</template>

<script lang="ts">
import { useFeed } from '@/store/feed'
import { storeToRefs } from 'pinia'
import { defineComponent, ref } from 'vue'

import BaseSidebar from '@/components/BaseSidebar.vue'
import SettingsSidebar from '@/components/SettingsSidebar.vue'

export default defineComponent({
  name: 'BaseSite',
  components: {
    BaseSidebar,
    SettingsSidebar
  },
  setup () {
    const store = useFeed()
    const { videos } = storeToRefs(store)
    const showSidebar = ref(true)
    return {
      showSidebar,
      store,
      videos
    }
  },
  beforeMount () {
    // Check the user's sidebar settings
  },
  methods: {
    something () {
    }
  }
})
</script>

<style scoped>
body {
  background-color: #fbfbfb;
}

main {
  margin-top: 58px;
  margin-bottom: 58px;
}

@media (min-width: 991.98px) {
  main {
    padding-left: 240px;
  }

  footer {
    padding-left: 240px;
  }
}

/* Sidebar */
.sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  padding: 58px 0 0;
  box-shadow: 0 2px 5px 0 rgb(0 0 0 / 5%), 0 2px 10px 0 rgb(0 0 0 / 5%);
  width: 240px;
  z-index: 600;
}

@media (max-width: 991.98px) {
  .sidebar {
    width: 100%;
  }
}

.sidebar-sticky {
  position: relative;
  top: 0;
  height: calc(100vh - 48px);
  padding-top: 0.5rem;
  overflow-x: hidden;
  overflow-y: auto;
}

#back-to-top {
  position: fixed;
  z-index: 1000;
  top: 90%;
  right: 2%;
}

.sidebar-enter-active,
.sidebar-leave-active {
  transition: opacity .4s ease-in-out;
}

.sidebar-enter-from,
.sidebar-leave-to {
  opacity: 0;
  transform: translateX(-100%);
}

.sidebar-enter-to,
.sidebar-leave-from {
  opacity: 1;
  transform: translateX(0%);
}
</style>
