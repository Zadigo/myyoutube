<template>
  <div class="flex items-center justify-left">
    <VoltButton size="large" color="primary" class="me-1" rounded @click="handleLike">
      <Icon v-if="requestData.liked" name="i-fa7-solid:thumbs-up" class="mr-2" />
      <Icon v-else name="i-fa7-regular:thumbs-up" class="mr-2" />
      Like <span class="font-bold">145.3k</span>
    </VoltButton>

    <VoltButton size="large" color="primary" class="me-3" rounded @click="handleUnlike">
      <Icon v-if="requestData.unliked" name="i-fa7-solid:thumbs-down" class="mr-2" />
      <Icon v-else name="i-fa7-regular:thumbs-down" class="mr-2" />
      Dislike <span class="font-bold">15</span>
    </VoltButton>
    
    <!-- Extra Actions -->
    <VoltDropdownButton id="more-actions" :items="menuItems">
      More
    </VoltDropdownButton>

    <VoltDropdownButton v-if="requestData.subscription.active" id="more-actions" :items="subscribeMenuItems" rounded>
      <Icon name="i-fa7-solid:bell-slash" />
    </VoltDropdownButton>

    <VoltButton v-else size="large" color="light" class="ml-5" @click="handleSubscription">
      Subscribe
    </VoltButton>
  </div>
</template>

<script lang="ts" setup>
import { inject, ref, watch } from 'vue'
import { setDoc, updateDoc, doc, getDoc } from 'firebase/firestore'
import type { Playlist, VideoInfo, VideoMenuItem } from '~/types'
import type { DefaultVideoMenuActions } from '~/data'

const menuItems: VideoMenuItem[] = [
  {
    label: 'Store',
    icon: 'i-fa7-solid:store'
  },
  {
    label: 'Download',
    icon: 'i-fa7-solid:download'
  },
  {
    label: 'Save',
    icon: 'i-fa7-solid:save'
  },
  {
    label: 'Gift',
    icon: 'i-fa7-solid:gift'
  },
  {
    label: 'Donate',
    icon: 'i-fa7-solid:dollar-sign'
  },
  {
    label: 'Share',
    icon: 'i-fa7-solid:share'
  },
  {
    label: 'Recommendations',
    icon: 'i-fa7-solid:star'
  },
  {
    label: 'Community note',
    icon: 'i-fa7-solid:note-sticky'
  },
  {
    label: 'Fact check',
    icon: 'i-fa7-solid:building-shield'
  },
  {
    label: 'Report',
    icon: 'i-fa7-solid:store'
  }
]

const subscribeMenuItems: { label: string, icon: string }[] = [
  {
    label: 'All',
    icon: 'i-fa7-solid:i-fa7-solid:bullhorn'
  },
  {
    label: 'None',
    icon: 'i-fa7-solid:i-fa7-solid:bell-slash'
  },
  {
    label: 'Unsubscribe',
    icon: 'i-fa7-solid:i-fa7-solid:user-minus'
  }
]

const db = useFirestore()

const viewingProfileId = useCookie('vp_id')
const { $client } = useNuxtApp()
const route = useRoute()
const router = useRouter()

const emit = defineEmits({
  action (_method: DefaultVideoMenuActions) {
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
