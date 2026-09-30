<template>
  <section id="studio" class="mx-auto">
    <u-card class="shadow-sm">
      <template #header>
        <div class="flex justify-between gap-4 items-center p-5 border-b border-slate-50">
          <div class="actions">
            <u-button to="/studio/upload" icon="i-fa7-solid:upload" class="me-2">
              Upload
            </u-button>

            <u-button to="/studio/statistics" class="me-2">
              <Icon name="i-fa7-solid:chart-simple" class="me-2" />
              Statistics
            </u-button>
          </div>

          <form id="search" @submit.prevent>
            <u-input v-model="search" placeholder="Search" aria-placeholder="Search" />
          </form>
        </div>
      </template>

      <template v-if="userVideos && userVideos.length > 0">
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

              <p class="flex justify-left text-muted">
                <span>4456 vues</span> - <span class="mx-2">400 likes</span>
              </p>
            </div>

            <div class="actions">
              <u-button color="primary" icon="i-fa7-solid:pen" />
              <u-button color="primary" icon="i-fa7-solid:ellipsis-vertical" />
            </div>
          </article>
        </div>
      </template>

      <template v-else>
        <h1>No videos</h1>
      </template>
    </u-card>
  </section>
</template>

<script lang="ts" setup>
const { data: userVideos, execute } = useAsyncData<VideoInfo[]>('user-videos', async () => await $fetch('/api/studio/videos', {
  method: 'GET'
}))

onBeforeMount(async () => {
  await execute()
})

const search = ref<string>('')

const searchedVideos = computed(() => {
  if (userVideos.value && search.value) {
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
</script>
