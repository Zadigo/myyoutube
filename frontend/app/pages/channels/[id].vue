<template>
  <section id="channel">
    <div class="wrapper">
      <v-carousel v-if="hasCarousel">
        <v-carousel-item src="https://cdn.vuetifyjs.com/images/cards/docks.jpg" cover />
        <v-carousel-item src="https://cdn.vuetifyjs.com/images/cards/hotel.jpg" cover />
        <v-carousel-item src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" cover />
      </v-carousel>

      <v-img v-else src="https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(22).webp" />

      <div class="information">
        <h1 class="text-light">
          {{ currentChannel?.name }}
        </h1>

        <p class="text-light fw-light">
          310 vidéos
        </p>

        <v-btn rounded="xl">
          <font-awesome :icon="['fas', 'fa-plus']" class="me-2" />
          Subscribe
        </v-btn>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { ref } from 'vue';
import type { UserChannel } from '~/apps/types';

const route = useRoute()
const { client } = useAxiosClient()
const store = useChannels()
const { currentChannel } = storeToRefs(store)
const hasCarousel = ref(false)

async function requestUserChannel () {
  try {
    const channelID = route.params.id
    const response = await client.post<UserChannel>(`channels/${channelID}`)
    currentChannel.value = response.data
  } catch {
    // Handle error
  }
}

onBeforeMount(async () => {
  await requestUserChannel()
})
</script>

<style lang="scss" scoped>
.wrapper {
  position: relative;
  background-color: black;
}

.information {
  position: absolute;
  padding: 2rem;
  top: 0;
  left: 0;
}
</style>
