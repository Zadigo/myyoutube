<template>
  <base-site-vue>
    <section id="playlists" class="d-flex justify-content-start align-items-start">
      <div v-if="showPlaylist" class="card" style="width: 380px;">
        <img src="https://via.placeholder.com/500" class="card-img-top" alt="Image 8" />
        <div class="card-header d-flex justify-content-between align-items-center">
          <button type="button" class="btn btn-light shadow-none" @click="showPlaylist = false">
            <font-awesome-icon icon="fa-solid fa-arrow-left" />
          </button>

          <button type="button" class="btn btn-light shadow-none">
            <font-awesome-icon icon="fa-solid fa-share" />
          </button>
        </div>
        <div class="card-body">
          <h4 class="card-title">Item name</h4>
          <div class="card-text">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque, est, 
            nihil soluta unde, provident sed molestias suscipit repellat ipsam iure quisquam 
            enim impedit quas totam ea quaerat modi at vero?
          </div>
        </div>

        <div class="card-footer">
          Google
        </div>
      </div>

      <div v-else class="wrapper" style="height: 100vh;">
        <div class="d-flex flex-column align-items-stretch flex-shrink-0 bg-white" style="width: 380px;">
          <div class="list-group list-group-flush border-bottom scrollarea">
            <a v-for="i in 5" :key="i" href :class="[i === 1 ? 'active' : null]" class="list-group-item list-group-item-action py-3 lh-sm" aria-current="true" @click.prevent="showPlaylist = true">
              <div class="d-flex w-100 align-items-center justify-content-between">
                <strong class="mb-1">List group item heading</strong>
                <small>Wed</small>
              </div>
              <div class="col-10 mb-1 small">Some placeholder content in a paragraph below the heading and date.</div>
            </a>
          </div>
        </div>
      </div>
      
      <section id="videos" class="ms-3">
        <div class="card mb-2">
          <div class="card-body text-right">
            <base-dropdown-button-vue :button-name="'sort'" :color="'light'" :items="[{ name: 'Newest' }, { name: 'Oldest' }, { name: 'Most popular' }]" @dropdown-click="dropdownClick" />
          </div>
        </div>

        <div v-for="i in 15" :key="i" class="card mb-1">
          <div class="card-body">
            Paul
          </div>
        </div>
      </section>
    </section>
  </base-site-vue>
</template>


<script>
import BaseDropdownButtonVue from '@/layouts/BaseDropdownButton.vue'
import BaseSiteVue from '../layouts/BaseSite.vue'

export default {
  name: 'PlaylistsView',
  components: {
    BaseDropdownButtonVue,
    BaseSiteVue
  },
  data () {
    return {
      showPlaylist: false
    }
  }
}
</script>

<style scoped>
.playlists {
  position: relative;
}

#videos {
  width: 50%;
}

.wrapper {
  position: sticky;
  top: 0;
  left: 0;
  height: 100vh;
}
</style>
