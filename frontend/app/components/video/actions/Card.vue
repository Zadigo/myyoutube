<template>
  <VoltCard>
    <template #content>
      <ClientOnly>
        <div v-if="currentVideo">
          <h1 class="font-bold">
            {{ currentVideo.title }}
          </h1>
        </div>
        <VoltSkeleton v-else height="50px" />

        <div v-if="currentVideo" class="flex justify-between items-center mt-3">
          <div v-if="currentVideo.user_channel" id="left" class="flex justify-left items-center gap-3">
            <NuxtLink :to="`/channels/${currentVideo.user_channel?.reference}`">
              <VoltAvatar image="/avatars/avatar1.png" size="xlarge" shape="circle" alt="" />
            </NuxtLink>
            
            <div class="wrapper">
              <h3 class="font-bold mb-1">
                103M views
              </h3>

              <p class="font-light text-secondary">
                20 months ago
              </p>
            </div>
          </div>
          
          <VideoActionsButtons />
        </div>
        <VoltSkeleton v-else height="50px" />
      </ClientOnly>
    </template> 
  </VoltCard>
</template>

<script lang="ts" setup>
import type { DefaultVideoMenuActions } from '~/data';
import type { Playlist, VideoInfo } from '~/types'

defineEmits<{ action: [method: DefaultVideoMenuActions], 'update-playlists': [data: Playlist[]] }>()

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

// const { execute } = useFetch('/api/playlists', {
//   method: 'get',
//   immediate: false,
//   async transform(data: Playlist[]) {
//     if (viewingProfileId.value) {
//       try {
//         const playlistDocRef = doc(db, 'playlists', viewingProfileId.value)
//         const docSnap = await getDoc(playlistDocRef)
  
//         if (docSnap.exists()) {
//           await setDoc(playlistDocRef, { playlists: data })
//         } else {
//           await updateDoc(playlistDocRef, { playlists: data })
//         }
//       } catch(e) {
//         console.error(e)
//       }
//     }

//     playlists.value = data
//     emit('update-playlists', data)
//     return data
//   }
// })
</script>
