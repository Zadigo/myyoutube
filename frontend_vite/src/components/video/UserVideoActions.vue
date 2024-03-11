<template>
  <div class="col-12">
    <div class="card">
      <div class="card-body">
        <h1 class="h4">When you realize ON AIR that your sister stole your watch</h1>
        <div class="d-flex justify-content-between align-items-center mt-3">
          <div id="left" class="d-flex justify-content-left gap-4">
            <router-link :to="{ name: 'channel_details', params: { id: 'ch_noienozinfoz' } }" aria-label="">
              <img src="/avatar1.png" class="img-fluid rounded-circle" width="50" height="50" alt="">
            </router-link>
            <h3 class="h6">User name</h3>
          </div>

          <div id="right">
            <v-btn size="large" rounded="xl" color="primary" class="me-1" flat @click="handleLike">
              <font-awesome-icon v-if="isLiked" icon="fas fa-thumbs-up" class="mr-2" />
              <font-awesome-icon v-else icon="far fa-thumbs-up" class="mr-2" />
              Like
            </v-btn>

            <v-btn size="large" rounded="xl" color="primary" class="me-3" flat @click="handleLike">
              <font-awesome-icon v-if="isDisliked" icon="fas fa-thumbs-down" class="mr-2" />
              <font-awesome-icon v-else icon="far fa-thumbs-down" class="mr-2" />
              Dislike
            </v-btn>

            <v-menu transition="slide-x-transition">
              <template v-slot:activator="{ props }">
                <v-btn size="large" rounded="xl" v-bind="props" color="primary" flat>
                  <font-awesome-icon icon="fas fa-caret-down" class="mr-2" />
                  More
                </v-btn>
              </template>

              <v-list>
                <v-list-item v-for="menuItem in menuItems" :key="menuItem.name" :value="menuItem" @click="handleMoreAction(menuItem)">
                  <v-list-item-title>
                    <font-awesome-icon :icon="[ 'fas', menuItem.icon ]" class="me-2" />
                    {{ menuItem.name }}
                  </v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
            
            <v-menu v-if="isSubscribed" transition="slide-x-transition">
              <template v-slot:activator="{ props }">
                <v-btn v-bind="props" size="large" rounded="xl" color="secondary" class="ml-5" flat>
                  <font-awesome-icon icon="fas fa-bell-slash" />
                </v-btn>
              </template>

              <v-list>
                <v-list-item value="All">
                  <v-list-item-title>
                    <font-awesome-icon icon="fas fa-bullhorn" class="me-2" />
                    All
                  </v-list-item-title>
                </v-list-item>

                <v-list-item value="None">
                  <v-list-item-title>
                    <font-awesome-icon icon="fas fa-bell-slash" class="me-2" />
                    None
                  </v-list-item-title>
                </v-list-item>
                
                <v-list-item value="Unsubsribe" @click="handleSubscription">
                  <v-list-item-title>
                    <font-awesome-icon icon="fas fa-user-minus" class="me-2" />
                    Unsubscribe
                  </v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>

            <v-btn v-else size="large" rounded="xl" color="secondary" class="ml-5" flat @click="handleSubscription">
              Subscribe
            </v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { inject, ref } from 'vue'
const menuItems = [
  {
    name: 'Store',
    icon: 'fa-store'
  },
  {
    name: 'Download',
    icon: 'fa-download'
  },
  {
    name: 'Save',
    icon: 'fa-save'
  },
  {
    name: 'Gift',
    icon: 'fa-gift'
  },
  {
    name: 'Donate',
    icon: 'fa-dollar-sign'
  },
  {
    name: 'Share',
    icon: 'fa-share'
  },
  {
    name: 'Recommendations',
    icon: 'fa-star'
  },
  {
    name: 'Report',
    icon: 'fa-store'
  }
]

export default {
  name: 'UserVideoActions',
  emits: {
    classify () {
      return true
    },
    report () {
      return true
    },
    gifts () {
      return true
    }
  },
  setup () {
    const isSubscribed = ref(false)
    const isLiked = ref(false)
    const isUnliked = ref(false)

    const currentVideo = inject('currentVideo')

    return {
      currentVideo,
      isLiked,
      isUnliked,
      isSubscribed,
      menuItems
    }
  },
  methods: {
    async handleLike () {
      this.isLiked = !this.isLiked
    },
    handleMoreAction (action) {
      switch (action.name) {
        case 'Recommendations':
          this.$emit('classify')
          break

        case 'Report':
          this.$emit('report')
          break

        case 'Gift':
          this.$emit('gifts')
          break
      
        default:
          break
      }
      console.log(action)
    },
    handleSubscription () {
      this.isSubscribed = !this.isSubscribed
    }
  }
}
</script>
