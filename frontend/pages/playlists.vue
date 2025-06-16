<template>
  <section id="playlists" class="container px-5">
    <div class="row">
      <!-- Playlist Details -->
      <div class="col-5">
        <!-- Details -->
        <div v-if="showPlaylistDetails" class="card shadow-sm">
          <div class="card-body">
            <v-img src="/avatar1.png" />

            <v-btn color="primary" variant="outlined" rounded="xl" class="mt-4" @click="showPlaylistDetails=false">
              <font-awesome icon="arrow-left" />
            </v-btn>
          </div>

          <hr>

          <div v-if="currentPlaylist" class="card-body">
            <h3>{{ currentPlaylist.name }}</h3>
            
            <p v-if="currentPlaylist.description" class="fw-light">
              {{ currentPlaylist.description }}
            </p>

            <p v-else class="">
              No description
            </p>
          </div>
        </div>
        
        <!-- List -->
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
                <article :data-id="playlist.id" :aria-labelledby="playlist.name">
                  <p class="fw-bold">{{ playlist.name }}</p>
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
          <div class="card-body">
            Select a playlist to display
          </div>
        </header>

        <!-- Videos -->
        <div class="row mt-5">
          <div v-if="hasVideos" class="col-12">
            <article v-for="video in playlistVideos" :key="video.id" :aria-labelledby="video.title" class="card shadow-sm mb-2">
              <div class="card-body p-2">
                <div class="d-flex justify-content-around align-items-center">
                  <NuxtLink :to="`/videos/${video.video_id}`">
                    <div class="video">
                      <v-img src="/avatar3.png" width="140" />
                    </div>
                  </NuxtLink>

                  <div class="information">
                    <NuxtLink :to="`/videos/${video.video_id}`">
                      <h3 class="h4">
                        {{ video.title }}
                      </h3>
                    </NuxtLink>

                    <NuxtLink :to="`/channels/${video.user_channel.id}`" aria-label="">
                      <p class="fw-bold">
                        {{ video.user_channel.name }}
                      </p>
                    </NuxtLink>

                    <p v-if="video.description">
                      {{ video.description }}
                    </p>
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
      <v-dialog v-model="showCreatePlaylist" max-width="500" @close="showCreatePlaylist=false">
        <v-card>
          <v-card-text>
            <v-form @submit.prevent>
              <VoltInputText v-model="requestData.name" placeholder="Name" variant="outlined" />
              <VoltInputText v-model="requestData.description" placeholder="Description" variant="outlined" />
              <v-switch v-model="requestData.is_intelligent" label="Private" inset hide-details />

              <div v-show="isIntelligent" id="intelligent-functionnalities" class="mt-4">
                <div class="d-flex gap-2">
                  <v-select :items="videoDetails" variant="outlined" />
                  <v-select placeholder="Operator" variant="outlined" />
                  <VoltInputText placeholder="Value" variant="outlined" />
                </div>
              </div>
            </v-form>
          </v-card-text>

          <v-card-actions>
            <v-btn @click="showCreatePlaylist=false">Close</v-btn>
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
import { z } from 'zod'

import type { Playlist, PlaylistVideo } from '~/types'

const { $client } = useNuxtApp()

const videoDetails = [
  'Name',
  'Author',
  'Release Date'
] as const

type VideoDetails = (typeof videoDetails)[number]

const requestDataSchema = z.object({
  name: z.string().nullable(),
  description: z.string().nullable(),
  is_intelligent: z.boolean()
})

type RequestData = z.infer<typeof requestDataSchema>

const showCreatePlaylist = ref<boolean>(false)
const isIntelligent = ref<boolean>(false)
const showPlaylistDetails = ref<boolean>(false)

const currentPlaylist = ref<Playlist>()
const playlists = ref<Playlist[]>([])
const playlistVideos = ref<PlaylistVideo[]>([])

const requestData = ref<RequestData>({
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

const { execute } = useFetch<Playlist[]>('/api/playlists', {
  baseURL: useRuntimeConfig().public.djangoProdUrl,
  query: {}
})

/**
 * Create a new playlist
 * 
 * @param [intelligent=false] Whether the playlist is intelligent or not 
 */
async function requestCreatePlaylist(intelligent: boolean = false) {
  try {
    const response = await $client<Playlist>('/playlists/create', {
      method: 'POST',
      body: requestData.value,
    })

    playlists.value.push(response)
    
    showCreatePlaylist.value = false

    requestData.value = {
      name: null,
      description: null,
      is_intelligent: intelligent
    }
  } catch (e) {
    console.error(e)
  }
}

onMounted(async () => {
  await execute()
})
</script>
