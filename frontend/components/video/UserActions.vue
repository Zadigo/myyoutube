<template>
  <div class="col-12">
    <div class="card">
      <div class="card-body">
        <h1 :aria-label="currentVideo.title" class="h5 fw-bold">
          {{ currentVideo?.title }}
        </h1>

        <div v-if="currentVideo" class="d-flex justify-content-between align-items-center mt-3">
          <div v-if="currentVideo.user_channel" id="left" class="d-flex justify-content-left gap-4">
            <!-- <NuxtLink :to="`/channels/${currentVideo.user_channel?.reference}`" aria-label="">
              <img src="/avatar1.png" class="img-fluid rounded-circle" width="50" height="50" alt="">
            </NuxtLink> -->
            
            <div class="wrapper">
              <h3 class="h6 fw-bold mb-1" aria-label="User name">
                103M views
              </h3>

              <p class="fw-light text-secondary">
                20 months ago
              </p>
            </div>
          </div>

          <div id="right">
            <v-btn size="large" rounded="xl" color="primary" class="me-1" flat @click="handleLike">
              <font-awesome v-if="requestData.liked" icon="thumbs-up" class="mr-2" />
              <font-awesome v-else :icon="['far', 'thumbs-up']" class="mr-2" />
              Like <span class="fw-bold">145.3k</span>
            </v-btn>

            <v-btn size="large" rounded="xl" color="primary" class="me-3" flat @click="handleUnlike">
              <font-awesome v-if="requestData.unliked" icon="thumbs-down" class="mr-2" />
              <font-awesome v-else :icon="['far', 'thumbs-down']" class="mr-2" />
              Dislike <span class="fw-bold">15</span>
            </v-btn>
            
            <!-- Extra Actions -->
            <v-menu transition="slide-x-transition">
              <template #activator="{ props }">
                <v-btn size="large" rounded="xl" v-bind="props" color="primary" flat>
                  <font-awesome icon="caret-down" class="mr-2" />
                  More
                </v-btn>
              </template>

              <v-list>
                <v-list-item v-for="menuItem in menuItems" :key="menuItem.name" :value="menuItem" @click="handleMoreAction(menuItem)">
                  <v-list-item-title>
                    <font-awesome :icon="[ 'fas', menuItem.icon ]" class="me-2" />
                    {{ menuItem.name }}
                  </v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
            
            <v-menu v-if="requestData.subscription.active" transition="slide-x-transition">
              <template #activator="{ props }">
                <v-btn v-bind="props" size="large" rounded="xl" color="secondary" class="ml-5" flat>
                  <font-awesome icon="bell-slash" />
                </v-btn>
              </template>

              <v-list>
                <v-list-item value="All">
                  <v-list-item-title>
                    <font-awesome icon="bullhorn" class="me-2" @click="handleSubscriptionMode('All')" />
                    All
                  </v-list-item-title>
                </v-list-item>

                <v-list-item value="None">
                  <v-list-item-title>
                    <font-awesome icon="bell-slash" class="me-2" @click="handleSubscriptionMode('None')" />
                    None
                  </v-list-item-title>
                </v-list-item>
                
                <v-list-item value="Unsubsribe" @click="handleSubscription">
                  <v-list-item-title>
                    <font-awesome icon="user-minus" class="me-2" />
                    Unsubscribe
                  </v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>

            <v-btn v-else size="large" rounded="xl" color="light" class="ml-5" flat @click="handleSubscription">
              Subscribe
            </v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { inject, ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import type { Playlist, VideoInfo, VideoMenuAction, VideoMenuItem } from '~/types';

const menuItems: VideoMenuItem[] = [
  {
    name: 'Store',
    icon: 'store'
  },
  {
    name: 'Download',
    icon: 'download'
  },
  {
    name: 'Save',
    icon: 'save'
  },
  {
    name: 'Gift',
    icon: 'gift'
  },
  {
    name: 'Donate',
    icon: 'dollar-sign'
  },
  {
    name: 'Share',
    icon: 'share'
  },
  {
    name: 'Recommendations',
    icon: 'star'
  },
  {
    name: 'Community note',
    icon: 'note-sticky'
  },
  {
    name: 'Fact check',
    icon: 'building-shield'
  },
  {
    name: 'Report',
    icon: 'store'
  }
]

const route = useRoute()
const router = useRouter()

const emit = defineEmits({
  // classify () {
  //   return true
  // },
  // report () {
  //   return true
  // },
  // gifts () {
  //   return true
  // },
  // save () {
  //   return true
  // }
  action (_method: VideoMenuAction) {
    return true
  }
})

const requestData = ref({
  liked: false,
  unliked: false,
  subscription: {
    active: false,
    mode: null
  }
})

const currentVideo = inject<VideoInfo>('currentVideo')
const playlists = ref<Playlist[]>([])

watch(requestData.value, (n) => {
  if (!n.subscription.active) {
    requestData.value.subscription.mode = null
  }
})

/**
 * 
 */
async function handleLike () {
  requestData.value.liked = !requestData.value.liked
}

/**
 * 
 */
async function handleUnlike () {
  requestData.value.unliked = !requestData.value.unliked
}

/**
 * 
 */
async function handleSubscription () {
  requestData.value.subscription.active = !requestData.value.subscription.active
}

/**
 * 
 */
async function handleSave () {
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
    emit('save', simplePlaylists)
  } catch (e) {
    console.log('requestSaveToPlaylist', e)
  }
}

/**
 * 
 */
function handleMoreAction (action: VideoMenuItem) {
  switch (action.name) {
    case 'Save':
      handleSave()
      break
      
    case 'Fact check':
      router.push({
        path: '/fact-checking',
        query: {
          v: route.params.id
        }
      })
      break
  
    default:
      emit('action', action.name)
      break
  }
}

/**
 * 
 */
function handleSubscriptionMode (mode: string) {
  requestData.value.subscription.mode = mode
}
</script>
