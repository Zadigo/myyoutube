<template>
  <VoltCard>
    <template #content>
      <h1 class="font-bold">
        {{ currentVideo?.title }}
      </h1>

      <div v-if="currentVideo" class="flex justify-between items-center mt-3">
        <div v-if="currentVideo.user_channel" id="left" class="d-flex justify-content-left gap-4">
          <!-- <NuxtLink :to="`/channels/${currentVideo.user_channel?.reference}`" aria-label="">
            <img src="/avatar1.png" class="img-fluid rounded-circle" width="50" height="50" alt="">
          </NuxtLink> -->
          
          <div class="wrapper">
            <h3 class="h6 font-bold mb-1" aria-label="User name">
              103M views
            </h3>

            <p class="font-light text-secondary">
              20 months ago
            </p>
          </div>
        </div>

        <div id="right">
          <VoltButton size="large" color="primary" class="me-1" @click="handleLike">
            <Icon v-if="requestData.liked" name="i-fa7-solid:thumbs-up" class="mr-2" />
            <Icon v-else name="i-fa7-regular:thumbs-up" class="mr-2" />
            Like <span class="fw-bold">145.3k</span>
          </VoltButton>

          <VoltButton size="large" color="primary" class="me-3" @click="handleUnlike">
            <Icon v-if="requestData.unliked" name="i-fa7-solid:thumbs-down" class="mr-2" />
            <Icon v-else name="i-fa7-regular:thumbs-down" class="mr-2" />
            Dislike <span class="fw-bold">15</span>
          </VoltButton>
          
          <!-- Extra Actions -->
          <v-menu transition="slide-x-transition">
            <template #activator="{ props }">
              <VoltButton size="large" v-bind="props" color="primary">
                <Icon name="i-fa7-solid:caret-down" class="mr-2" />
                More
              </VoltButton>
            </template>

            <v-list>
              <v-list-item v-for="menuItem in menuItems" :key="menuItem.name" :value="menuItem" @click="() => handleMoreAction(menuItem)">
                <v-list-item-title>
                  <Icon :name="menuItem.icon" class="me-2" />
                  {{ menuItem.name }}
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
          
          <v-menu v-if="requestData.subscription.active" transition="slide-x-transition">
            <template #activator="{ props }">
              <VoltButton v-bind="props" size="large" color="secondary" class="ml-5">
                <Icon name="i-fa7-solid:bell-slash" />
              </VoltButton>
            </template>

            <v-list>
              <v-list-item value="All">
                <v-list-item-title>
                  <Icon name="i-fa7-solid:bullhorn" class="me-2" @click="handleSubscriptionMode('All')" />
                  All
                </v-list-item-title>
              </v-list-item>

              <v-list-item value="None">
                <v-list-item-title>
                  <Icon name="i-fa7-solid:bell-slash" class="me-2" @click="handleSubscriptionMode('None')" />
                  None
                </v-list-item-title>
              </v-list-item>
              
              <v-list-item value="Unsubsribe" @click="handleSubscription">
                <v-list-item-title>
                  <Icon name="i-fa7-solid:user-minus" class="me-2" />
                  Unsubscribe
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>

          <VoltButton v-else size="large" color="light" class="ml-5" @click="handleSubscription">
            Subscribe
          </VoltButton>
        </div>
      </div>
    </template>
  </VoltCard>
</template>

<script lang="ts" setup>
import { inject, ref, watch } from 'vue'
import { setDoc, updateDoc, doc, getDoc } from 'firebase/firestore'
import type { Playlist, VideoInfo, VideoMenuAction, VideoMenuItem } from '~/types'

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

const db = useFirestore()

const viewingProfileId = useCookie('vp_id')
const { $client } = useNuxtApp()
const route = useRoute()
const router = useRouter()

const emit = defineEmits({
  action (_method: VideoMenuAction) {
    return true
  },
  'update-playlists'(_data: Playlist[]) {
    return true
  }
})

const currentVideo = inject<VideoInfo>('currentVideo')

const playlists = ref<Playlist[]>([])
const requestData = ref({
  liked: false,
  unliked: false,
  subscription: {
    active: false,
    mode: null
  }
})


watch(requestData.value, (values) => {
  if (!values.subscription.active) {
    requestData.value.subscription.mode = null
  }
})

// Sends a request to to indicate that the
// video was liked or disliked by the user
async function handleLikeDislike() {
  try {
    await $client.post('/fake-endpoint', requestData.value)
  } catch (e) {
    console.log(e)
  }
}

/**
 * 
 */
async function handleLike () {
  requestData.value.liked = !requestData.value.liked
  await handleLikeDislike()
}

/**
 * 
 */
async function handleUnlike () {
  requestData.value.unliked = !requestData.value.unliked
  await handleLikeDislike()
}

/**
 * 
 */
async function handleSubscription () {
  requestData.value.subscription.active = !requestData.value.subscription.active
  await handleLikeDislike()
}

const { execute } = useFetch('/api/playlists', {
  method: 'get',
  immediate: false,
  async transform(data: Playlist[]) {
    if (viewingProfileId.value) {
      try {
        const playlistDocRef = doc(db, 'playlists', viewingProfileId.value)
        const docSnap = await getDoc(playlistDocRef)
  
        if (docSnap.exists()) {
          await setDoc(playlistDocRef, { playlists: data })
        } else {
          await updateDoc(playlistDocRef, { playlists: data })
        }
      } catch(e) {
        console.error(e)
      }
    }

    playlists.value = data
    emit('update-playlists', data)
    return data
  }
})

/**
 * 
 */
function handleMoreAction (action: VideoMenuItem) {
  switch (action.name) {
    case 'Save':
      execute()
      emit('action', action.name)
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
