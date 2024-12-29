<template>
  <section :class="{ full: !showSidebar }" class="dashboard">
    <header>
      <!-- Sidebar -->
      <Transition tag="div" name="sidebar" mode="out-in">
        <nav v-if="showSidebar" id="sidebar" class="collapse d-lg-block sidebar collapse bg-white">
          <div class="position-sticky">
            <SidebarsBase v-if="$route.meta.requiresSettingsNav" />
            <SidebarsBase v-else />
          </div>
        </nav>
      </Transition>

      <!-- Navbar -->
      <nav v-show="$route.meta.requiresNav" id="main-navbar" class="navbar navbar-expand-lg fixed-top navbar-light bg-white">
        <div class="container-fluid">
          <button class="navbar-toggler" type="button" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
            <font-awesome icon="bars" />
          </button>
          
          <v-btn rounded="xl" text flat @click="showSidebar = !showSidebar">
            <font-awesome icon="bar" />
          </v-btn>

          <NuxtLink to="/" class="navbar-brand">
            My Youtube
          </NuxtLink>

          <ul class="navbar-nav ms-auto d-flex flex-row">
            <v-avatar image="/avatar1.png" size="35" />
          </ul>
        </div>
      </nav>
    </header>

    <main>
      <div class="container pt-4">
        <slot />
      </div>
    </main>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const showSidebar = ref(true)
</script>

<style lang="scss" scoped>
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
