<template>
  <base-site-vue>
    <section id="playlists">
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-12 col-md-8 offset-md-2 mb-2">
            <div class="card shadow-none">
              <div class="card-body">
                <ul class="nav nav-pills nav-fill">
                  <li v-for="(item, i) in items" :key="i" class="nav-item">
                    <a :class="[item.component === currentComponent ? 'active' : null ]" class="nav-link" aria-current="page" href @click.prevent="currentComponent = item.component">
                      {{ item.name }}
                      <span v-if="i > 0" class="badge bg-primary rounded-pill">14</span>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <!-- TODO: Make this components -->
          <component :is="currentComponent" />
        </div>
      </div>
    </section>
  </base-site-vue>
</template>


<script>
import BaseSiteVue from '../layouts/BaseSite.vue'
import ListAllVue from '@/components/notifications/ListAll.vue'
import ListMessagesVue from '@/components/notifications/ListMessages.vue'
import ListUploadsVue from '@/components/notifications/ListUploads.vue'

export default {
  name: 'NotificationsView',
  components: {
    BaseSiteVue,
    ListAllVue,
    ListMessagesVue,
    ListUploadsVue
  },
  data () {
    return {
      items: [
        { component: 'list-all-vue', name: 'All' },
        { component: 'list-messages-vue', name: 'Messages' },
        { component: 'list-uploads-vue', name: 'Uploads' }
      ],
      currentComponent: 'list-all-vue'
    }
  }
}
</script>

<style scoped>
</style>
