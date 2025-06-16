<template>
  <section id="studio" class="container px-5">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-header">
            <div class="d-flex justify-content-between gap-4 align-items-center">
              <div class="actions">
                <v-btn to="/studio/upload" class="me-2" color="secondary" variant="tonal" rounded="xl">
                  <font-awesome icon="upload" class="me-2" />
                  Upload
                </v-btn>

                <v-btn color="secondary" rounded="xl" variant="tonal">
                  <font-awesome icon="chart-simple" class="me-2" />
                  Statistics
                </v-btn>
              </div>

              <v-form id="search" style="width:30%;" @submit.prevent>
                <VoltInputText v-model="search" placeholder="Search" aria-placeholder="Search" variant="outlined" hide-details />
              </v-form>
            </div>
          </div>

          <div v-if="userVideos.length > 0" class="card-body">
            <div class="list-group">
              <article v-for="video in searchedVideos" :key="video.id" :aria-label="video.title" class="list-group-item list-group-item-action p-4 d-flex gap-4 justify-content-left align-items-center">
                <img src="https://via.placeholder.com/100x100" class="img-fluid rounded" alt="">

                <div class="infos p-2 mx-1 flex-shrink-1">
                  <h5>
                    {{ video.title }}
                  </h5>

                  <p class="mb-2">
                    {{ video.description }}
                  </p>

                  <p class="d-flex justify-content-left text-muted">
                    <span>4456 vues</span> - <span class="mx-2">400 likes</span>
                  </p>
                </div>

                <div class="actions">
                  <v-btn color="primary" rounded="xl">
                    <font-awesome icon="pen" />
                  </v-btn>

                  <v-btn color="primary" rounded="xl">
                    <font-awesome icon="ellipsis-vertical" />
                  </v-btn>
                </div>
              </article>
            </div>
          </div>

          <div v-else class="card-body text-center">
            <h1>No videos</h1>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts" setup>
import type { VideoInfo } from '~/types';
import { onBeforeMount, ref } from 'vue';

const { $client } = useNuxtApp()

const userVideos = ref<VideoInfo[]>([])
const search = ref<string | null>(null)

const searchedVideos = computed(() => {
  if (search.value) {
    return userVideos.value.filter((video) => {
      if (search.value && search.value !== "") {
        return video.title.toLocaleLowerCase().includes(search.value?.toLowerCase())
      } else {
        return userVideos.value
      }
    })
  } else {
    return userVideos.value
  }
})

/**
 * Get all the details for the current video 
 */
async function requestUserVideos () {
  try {
    const response = await $client.get(`videos/studio/videos`)
    userVideos.value = response.data
  } catch (e) {
    console.log(e)
  }
}

onBeforeMount(async () => {
  await requestUserVideos()
})
</script>
