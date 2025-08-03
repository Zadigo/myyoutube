<template>
  <section id="playlists" class="grid grid-cols-2 gap-2">
    <!-- Playlist Details -->
    <div>
      <PlaylistsDetails v-if="showPlaylistDetails" @show:details="select" />
      <PlaylistsList v-else @show:create="openCreationDialog" @show:details="select" />
    </div>
    
    <!-- Videos -->
    <div>
      <header>
        <VoltCard>
          <template #header>
            Select a playlist to display
          </template>
        </VoltCard>
      </header>

      <!-- Videos -->
      <div class="mt-5">
        <div v-if="hasVideos">
          <article v-for="video in playlistVideos" :key="video.id" class="shadow-sm mb-2">
            <VoltCard>
              <template #content>
                <div class="p-2">
                  <div class="flex justify-left gap-2 items-center">
                    <NuxtLink :to="`/videos/${video.video_id}`">
                      <div class="video">
                        <VoltAvatar src="/avatars/avatar1.png" shape="circle" size="large" />
                      </div>
                    </NuxtLink>

                    <div class="information">
                      <NuxtLink :to="`/videos/${video.video_id}`">
                        <h3 class="text-2xl font-bold">
                          {{ video.title }}
                        </h3>
                      </NuxtLink>

                      <NuxtLink :to="`/channels/${video.user_channel.id}`">
                        <p class="font-bold">
                          {{ video.user_channel.name }}
                        </p>
                      </NuxtLink>

                      <p v-if="video.description" class="text-sm">
                        {{ video.description }}
                      </p>
                    </div>
                  </div>
                </div>
              </template>
            </VoltCard>
          </article>
        </div>
      </div>
    </div>

    <!-- Modals -->
    <ClientOnly>
      <VoltDialog v-model:visible="showCreatePlaylist" modal>
        <form @submit.prevent>
          <div class="space-y-2">
            <VoltInputText v-model="newPlaylist.name" placeholder="Name" class="w-full" />
            <VoltInputText v-model="newPlaylist.description" placeholder="Description" class="w-full" />

            <VoltLabel>
              <VoltToggleSwitch v-model="newPlaylist.is_intelligent" />
              <label>Private</label>
            </VoltLabel>
          </div>

          <div v-show="isIntelligent" id="intelligent-functionnalities" class="mt-4">
            <div class="flex gap-2 p-4 bg-slate-50 rounded-md my-5">
              <VoltSelect :options="Array.from(intelligentVideoOptions)" />
              <VoltSelect placeholder="Operator" />
              <VoltInputText placeholder="Value" />
            </div>
          </div>
        </form>
        
        <VoltButton @click="showCreatePlaylist = false">
          Save
        </VoltButton>
      </VoltDialog>
    </ClientOnly>
  </section>
</template>

<script setup lang="ts">
import { useEditPlaylist } from '~/composables/use'

const showPlaylistDetails = ref<boolean>(false)

const playlistStore = usePlaylistStore()
const { playlists } = storeToRefs(playlistStore)

playlistStore.fetch()

const { showCreatePlaylist, isIntelligent, newPlaylist, create, select, openCreationDialog, currentPlaylist, intelligentVideoOptions, intelligentVideoOptionsMenuItem } = useEditPlaylist(playlists)

const playlistVideos = computed(() => currentPlaylist.value?.videos || [])
const hasVideos = computed(() => playlistVideos.value.length > 0)

provide('playlists', playlists)
provide('currentPlaylist', currentPlaylist)
</script>
