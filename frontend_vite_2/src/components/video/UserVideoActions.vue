<template>
  <div class="col-12">
    <div class="card">
      <div class="card-body">
        <h1 class="h4" aria-label="">
          {{ currentVideo?.title }}
        </h1>

        <div v-if="currentVideo" class="d-flex justify-content-between align-items-center mt-3">
          <div v-if="currentVideo.user_channel" id="left" class="d-flex justify-content-left gap-4">
            <router-link :to="{ name: 'channel_details', params: { id: currentVideo.user_channel?.reference } }" aria-label="">
              <img src="/avatar1.png" class="img-fluid rounded-circle" width="50" height="50" alt="">
            </router-link>

            <h3 class="h6" aria-label="User name">
              {{ currentVideo.user.get_full_name }}
            </h3>
          </div>

          <div id="right">
            <v-btn size="large" rounded="xl" color="primary" class="me-1" flat @click="handleLike">
              <font-awesome-icon v-if="requestData.liked" icon="fas fa-thumbs-up" class="mr-2" />
              <font-awesome-icon v-else icon="far fa-thumbs-up" class="mr-2" />
              Like
            </v-btn>

            <v-btn size="large" rounded="xl" color="primary" class="me-3" flat @click="handleUnlike">
              <font-awesome-icon v-if="requestData.unliked" icon="fas fa-thumbs-down" class="mr-2" />
              <font-awesome-icon v-else icon="far fa-thumbs-down" class="mr-2" />
              Dislike
            </v-btn>

            <v-menu transition="slide-x-transition">
              <template #activator="{ props }">
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
            
            <v-menu v-if="requestData.subscription.active" transition="slide-x-transition">
              <template #activator="{ props }">
                <v-btn v-bind="props" size="large" rounded="xl" color="secondary" class="ml-5" flat>
                  <font-awesome-icon icon="fas fa-bell-slash" />
                </v-btn>
              </template>

              <v-list>
                <v-list-item value="All">
                  <v-list-item-title>
                    <font-awesome-icon icon="fas fa-bullhorn" class="me-2" @click="handleSubscriptionMode('All')" />
                    All
                  </v-list-item-title>
                </v-list-item>

                <v-list-item value="None">
                  <v-list-item-title>
                    <font-awesome-icon icon="fas fa-bell-slash" class="me-2" @click="handleSubscriptionMode('None')" />
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

<script lang="ts">
import { Video } from '@/types/feed';
import { defineComponent, inject, ref } from 'vue'

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
    name: 'Community note',
    icon: 'fa-note-sticky'
  },
  {
    name: 'Report',
    icon: 'fa-store'
  }
]

export default defineComponent({
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
    },
    save () {
      return true
    }
  },
  setup () {
    const requestData = ref({
      liked: false,
      unliked: false,
      subscription: {
        active: false,
        mode: null
      }
    })

    const currentVideo = inject<Video>('currentVideo')

    const playlists = ref([])

    return {
      playlists,
      requestData,
      currentVideo,
      menuItems
    }
  },
  watch: {
    'requestData.subscription.active' (n) {
      if (!n) {
        this.requestData.subscription.mode = null
      }
    }
  },
  methods: {
    /**
     * 
     */
    async handleLike () {
      this.requestData.liked = !this.requestData.liked
    },
    /**
     * 
     */
    async handleUnlike () {
      this.requestData.unliked = !this.requestData.unliked
    },
    /**
     * 
     */
    async handleSubscription () {
      this.requestData.subscription.active = !this.requestData.subscription.active
    },
    /**
     * 
     */
    async handleSave () {
      try {
        let simplePlaylists

        if (this.$session.keyExists('simple_playlists')) {
          simplePlaylists = this.$session.retrieve('simple_playlists')
        } else {
          const response = await this.$client.get('/playlists/', {
            params: {
              simple: 1
            }
          })
          simplePlaylists = response.data
          this.$session.create('simple_playlists', simplePlaylists)
        }
        this.$emit('save', simplePlaylists)
      } catch (e) {
        console.log('requestSaveToPlaylist', e)
      }
    },
    /**
     * 
     */
    handleMoreAction (action) {
      switch (action.name) {
        case 'Recommendations':
          this.$emit('classify')
          break

        case 'Save':
          this.handleSave()
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
    /**
     * 
     */
    handleSubscriptionMode (mode) {
      this.requestData.subscription.mode = mode
    }
  }
})
</script>
