<template>
  <section id="channel">
    <div class="wrapper">

      <v-carousel v-if="hasCarousel">
        <v-carousel-item src="https://cdn.vuetifyjs.com/images/cards/docks.jpg" cover></v-carousel-item>
        <v-carousel-item src="https://cdn.vuetifyjs.com/images/cards/hotel.jpg" cover></v-carousel-item>
        <v-carousel-item src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" cover></v-carousel-item>
      </v-carousel>

      <v-img v-else src="https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(22).webp"></v-img>

      <div class="information">
        <h1 class="text-light">{{ currentChannel.name }}</h1>
        <p class="text-light fw-light">310 vidéos</p>

        <v-btn rounded="xl">
          <font-awesome-icon :icon="['fas', 'fa-plus']" class="me-2" />
          Subscribe
        </v-btn>
      </div>
    </div>
  </section>
</template>

<script>
import { ref } from 'vue'
import { useChannels } from '../store/channels'
import { storeToRefs } from 'pinia'

export default {
  name: 'ChannelPage',
  beforeRouteEnter (to, from, next) {
    next(vm => {
      console.log(vm)
    })
  },
  setup () {
    const store = useChannels()
    const { currentChannel } = storeToRefs(store)

    const hasCarousel = ref(false)

    return {
      currentChannel,
      hasCarousel
    }
  },
  mounted () {
    this.requestUserChannel()
  },
  methods: {
    async requestUserChannel () {
      try {
        const channelID = this.$route.params.id
        const response = await this.$client.post(`channels/${channelID}`)
        this.currentChannel = response.data
      } catch (e) {
        console.log(e)
      }
    },
  }
}
</script>

<style scoped>
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
