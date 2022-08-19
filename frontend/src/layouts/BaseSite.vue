<template>
  <section>
    <header>
      <!-- Sidebar -->
      <nav id="sidebar" link="sidebar" class="collapse d-lg-block sidebar collapse bg-white">
        <div class="position-sticky">
          <div class="list-group list-group-flush mx-3 mt-4">
            <!-- NOTE: Pass links to props -->
            <!-- <router-link :to="{ name: 'home_view' }" class="list-group-item list-group-item-action py-2 ripple" aria-current="true">
              <span class="mdi mdi-youtube me-3"></span>
              <span>Youtube</span>
            </router-link> -->
          </div>
        </div>
      </nav>

      <!-- Navbar -->
      <nav id="main-navbar" class="navbar navbar-expand-lg navbar-light bg-white fixed-top">
        <div class="container-fluid">
          <button class="navbar-toggler" type="button" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
            <i class="fas fa-bars"></i>
          </button>

          <router-link :to="{ name: 'home_view' }" class="navbar-brand">
            <img src="https://mdbootstrap.com/img/logo/mdb-transaprent-noshadows.png" height="25" loading="lazy" alt="Image 4" />
          </router-link>

          <ul class="navbar-nav ms-auto d-flex flex-row">
            <nav-item :to="{ name: 'account_view' }" link-name="Account" />
          </ul>
        </div>
      </nav>
    </header>

    <!-- Main -->
    <main>
      <div :class="bodyClasses" class="container pt-4">
        <slot></slot>
      </div>
    </main>

    <transition name="pop">
      <button v-if="!arrivedState.top" id="back-to-top" class="btn btn-primary btn-floating" type="button" @click="scrollToTop">
        <font-awesome-icon icon="fa-solid fa-arrow-up" />
      </button>
    </transition>

    <!-- Footer -->
    <base-footer-vue />
  </section>
</template>

<script>
import { provide, ref } from 'vue'

import BaseFooterVue from './BaseFooter.vue'
import NavItem from '../layouts/nav/NavItem.vue'

import { useDark, useScroll } from '@vueuse/core'
import { scrollToTop } from '@/composables/utils'

export default {
  name: 'BaseSite',
  components: {
    BaseFooterVue,
    NavItem
  },
  props: {
    bodyClasses: {
      type: String,
      required: false
    }
  },
  setup () {
    const target = ref(null)
    const { y, arrivedState } = useScroll(target)
    const { value } = useDark()
    provide('darkMode', value)
    return {
      darkMode: value,
      target,
      scrollToTop,
      scrollY: y,
      arrivedState
    }
  },
  mounted () {
    this.target = window.document
  }
}
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

.sidebar .active {
  border-radius: 5px;
  box-shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);
}

.router-link-exact-active {
  z-index: 2;
  color: #fff;
  background-color: #1266f1;
  border-color: #1266f1;
  border-radius: 5px;
  box-shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);
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

.pop-enter-active .pop-leave-active {
  transition: opacity .4s ease;
  transition: scale .2s ease;
}

.pop-enter-from,
.pop-leave-to {
  opacity: 0;
  transform: scale(1.2, 1.2);
}

.pop-enter-to,
.pop-leave-from {
  opacity: 1;
  transform: scale(1, 1);
}
</style>
