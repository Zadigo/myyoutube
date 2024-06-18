<template>
  <div class="col-12 mt-4">
    <div class="card">
      <div class="card-body">
        <div class="d-flex flex-row justify-content-around align-items-start gap-3">
          <router-link :to="{ name: 'channel_details', params: { id: currentVideo.user_channel?.reference } }" aria-label="">
            <img src="/avatar1.png" class="img-fluid rounded-circle" width="120" height="120" alt="">
          </router-link>

          <div class="information">
            <v-btn :to="{ name: 'channel_details', params: { id: currentVideo.user_channel?.reference } }" class="px-0" color="primary" variant="plain">
              <span class="fw-bold">Malika Andrews - ESPN</span>
              <font-awesome-icon icon="fa fa-circle-check" class="ms-4" />
            </v-btn>
            <p class="text-body-tertiary">345.6K subscribers</p>

            <v-sheet class="mx-auto" max-width="800px">
              <v-slide-group show-arrows>
                <v-slide-group-item v-for="n in 10" :key="n" v-slot="{ isSelected, toggle }">
                  <v-btn :color="isSelected ? 'success' : undefined" class="ma-2" rounded @click="toggle">
                    Options {{ n }}
                  </v-btn>
                </v-slide-group-item>
              </v-slide-group>
            </v-sheet>

            <p class="fw-light">
              Lorem, ipsum dolor sit amet consectetur adipisicing elit.
              Sequi porro iure repellat optio, ipsum ducimus veniam natus
              ipsam dolor, suscipit distinctio vero? Labore repellendus
              ipsum et cumque fuga? Ullam, nam! Lorem ipsum dolor sit amet
              consectetur adipisicing elit. Voluptates id pariatur
              fuga molestiae aperiam inventore repellendus, dolorum
              ducimus saepe fugiat minima quisquam. Deleniti, ratione?
              Quis et harum ullam ab nam.
            </p>

            <v-btn color="primary" variant="plain">
              <font-awesome-icon icon="fa fa-caret-down" class="me-2" />
              More
            </v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { inject } from 'vue'

export default {
  name: 'VideoInformation',
  setup () {
    const currentVideo = inject('currentVideo')
    return {
      currentVideo
    }
  }
}
</script>
