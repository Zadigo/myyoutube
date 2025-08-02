<template>
  <section :class="{ full: !showSidebar }" class="relative">
    <header>
      <!-- Sidebar -->
      <Transition tag="div" name="sidebar" mode="out-in">
        <nav v-if="showSidebar" id="sidebar" class="bg-white fixed top-0 left-0 bottom-0 p-3 shadow-md w-[240px] z-30">
          <SidebarsBase :links="navLinks" />
        </nav>
      </Transition>

      <!-- Navbar -->
      <nav v-show="$route.meta.requiresNav" class="bg-white fixed top-0 left-0 right-0 p-2 shadow-md z-40">
        <div class="container-fluid">
          <VoltButton class="navbar-toggler" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
            <Icon name="i-fa7-soli:bars" />
          </VoltButton>
          
          <VoltButton @click="showSidebar=!showSidebar">
            <Icon name="i-fa7-soli:bars" />
          </VoltButton>

          <NuxtLink to="/" class="navbar-brand">
            My Youtube
          </NuxtLink>

          <ul class="ms-auto flex">
            <VoltAvatar image="/avatar1.png" size="35" />
          </ul>
        </div>
      </nav>
    </header>

    <main class="my-10 ps-[calc(240px+1rem)] pe-2">
      <slot />
    </main>
  </section>
</template>

<script setup lang="ts">
const showSidebar = ref<boolean>(true)

const navLinks = [
  {
    name: 'Home',
    to: 'feed',
    icon: 'i-fa7-solid:home'
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
    icon: 'i-fa7-solid:chart-simple'
  }
]
</script>

<style lang="scss" scoped>
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
