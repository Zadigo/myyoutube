<template>
  <section id="playlists" class="container px-5">
    <div class="row">
      <!-- Playlist -->
      <div class="col-5">
        <!-- Playlist Details -->
        <div v-if="showPlaylistDetails" class="card shadow-sm">
          <div class="card-body">
            <v-img src="/avatar1.png" />

            <v-btn color="primary" variant="outlined" rounded="xl" class="mt-4" @click="showPlaylistDetails=false">
              <font-awesome icon="arrow-left" />
            </v-btn>
          </div>

          <hr>

          <div class="card-body">
            <h3>{{ currentPlaylist.title }}</h3>
            <p v-if="currentPlaylist.description" class="fw-light">{{ currentPlaylist.description }}</p>
            <p v-else class="">No description</p>
          </div>
        </div>
        
        <!-- Playlists -->
        <div v-else class="card shadow-sm">
          <div class="card-body">
            <v-btn class="me-2" color="primary" rounded="xl" size="small" flat @click="showCreatePlaylist=true">
              <font-awesome icon="plus" class="me-2" />
              Playlist
            </v-btn>

            <v-btn color="primary" rounded="xl" size="small" flat @click="isIntelligent = true, showCreatePlaylist = true">
              <font-awesome icon="star" class="me-2" />
              Intelligent playlist
            </v-btn>

            <hr>

            <div class="list-group">
              <a v-for="playlist in playlists" :key="playlist.id" href="#" class="list-group-item list-group-item-action p-3" @click.prevent="currentPlaylist = playlist, showPlaylistDetails = true">
                <article :data-id="playlist.id" :aria-labelledby="playlist.title">
                  <p class="fw-bold">{{ playlist.title }}</p>
                  <p v-if="playlist.description" class="fw-light m-0">
                    {{ playlist.description }}
                  </p>
                </article>
              </a>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Videos -->
      <div class="col-7">
        <header class="card shadow-sm">
          <div class="card-body" />
        </header>

        <!-- Videos -->
        <div class="row mt-5">
          <div v-if="hasVideos" class="col-12">
            <article v-for="video in playlistVideos" :key="video.id" :aria-labelledby="video.title" class="card shadow-sm mb-2">
              <div class="card-body p-2">
                <div class="d-flex justify-content-around align-items-center">
                  <router-link :to="{ name: 'video_details', params: { id: video.video_id } }">
                    <div class="video">
                      <v-img src="/avatar3.png" width="140" />
                    </div>
                  </router-link>

                  <div class="information">
                    <h3 class="h4">
                      {{ video.title }}
                    </h3>

                    <router-link :to="{ name: 'channel_details', params: { id: 'ch_noienozinfoz' } }" aria-label="">
                      <p class="fw-bold">The creator account</p>
                    </router-link>

                    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit.</p>
                  </div>
                </div>
              </div>
            </article>
          </div>
        </div>
      </div>
    </div>

    <!-- Modals -->
    <ClientOnly>
      <v-dialog v-model="showCreatePlaylist" max-width="500" @close="showCreatePlaylist = false">
        <v-card>
          <v-card-text>
            <v-form @submit.prevent>
              <v-text-field v-model="requestData.name" placeholder="Name" variant="outlined" />
              <v-text-field v-model="requestData.description" placeholder="Description" variant="outlined" />
              <v-switch v-model="requestData.is_intelligent" label="Private" inset hide-details />

              <div v-show="isIntelligent" id="intelligent-functionnalities" class="mt-4">
                <div class="d-flex gap-2">
                  <v-select :items="videoDetails" variant="outlined" />
                  <v-select placeholder="Operator" variant="outlined" />
                  <v-text-field placeholder="Value" variant="outlined" />
                </div>
              </div>
            </v-form>
          </v-card-text>

          <v-card-actions>
            <v-btn @click="showCreatePlaylist = false">Close</v-btn>
            <v-btn @click="requestCreatePlaylist">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </ClientOnly>
  </section>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { whenever } from '@vueuse/core'
import type { Playlist } from '~/types'

const videoDetails = [
  'Name',
  'Author',
  'Release Date'
]

const showCreatePlaylist = ref(false)
const isIntelligent = ref(false)
const showPlaylistDetails = ref(false)

const currentPlaylist = ref<Playlist>()
const playlists = ref<Playlist[]>([])
const playlistVideos = ref([])

const requestData = ref({
  name: null,
  description: null,
  is_intelligent: false
})

const hasVideos = computed(() => {
  return playlistVideos.value.length > 0
})

whenever(showPlaylistDetails, () => {
  if (currentPlaylist.value) {
    playlistVideos.value = currentPlaylist.value.videos
  }
})

watch(showCreatePlaylist, (n) => {
  if (!n) {
    isIntelligent.value = false
  }
})


useFetch('/api/playlists', {
  transform(data: Playlist[]) {
    playlists.value = data
    return data
  }
})

// async function requestPlaylists () {
//   try {
//     if (this.$session.keyExists('playlists')) {
//       this.playlists = this.$session.retrieve('playlists')
//     } else {
//       const response = await this.$client.get('/playlists/', this.requestData)
//       this.playlists = response.data
//       this.$session.create('playlists', this.playlists)
//     }
//   } catch (e) {
//     console.error('requestPlaylists', e)
//   }
// }

async function requestCreatePlaylist () {
  try {
    const response = await this.$client.post('/playlists/create', this.requestData)
    this.playlists.push(response.data)
    this.showCreatePlaylist = false
    this.requestData = {
      name: null,
      description: null,
      is_intelligent: false
    }
  } catch (e) {
    console.error(e)
  }
}

// onBeforeMount(async () => {
//   await requestPlaylists()
// })
</script>
