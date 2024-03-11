<template>
  <section id="playlists">
    <div class="row">
      <div class="col-5">
        <div v-if="showPlaylistDetails" class="card shadow-sm">
          <div class="card-body">
            <v-img src="/avatar1.png"></v-img>
            <v-btn color="primary" variant="outlined" rounded="xl" class="mt-4" @click="showPlaylistDetails = false">
              <font-awesome-icon :icon="[ 'fas', 'fa-arrow-left' ]" />
            </v-btn>
          </div>

          <hr>

          <div class="card-body">
            <h3>Item name</h3>
            <p class="fw-light">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque, est, nihil 
              soluta unde, provident sed molestias suscipit repellat ipsam iure quisquam enim 
              impedit quas totam ea quaerat modi at vero?
            </p>
          </div>
        </div>
        
        <div v-else class="card shadow-sm">
          <div class="card-body">
            <v-btn class="me-2" color="primary" rounded="xl" size="small" flat @click="showCreatePlaylist = true">
              <font-awesome-icon :icon="[ 'fas', 'fa-plus' ]" class="me-2" />
              Playlist
            </v-btn>

            <v-btn color="primary" rounded="xl" size="small" flat @click="isIntelligent = true, showCreatePlaylist = true">
              <font-awesome-icon :icon="[ 'fas', 'fa-star' ]" class="me-2" />
              Intelligent playlist
            </v-btn>

            <hr>

            <div class="list-group">
              <a v-for="i in 4" :key="i" href class="list-group-item list-group-item-action p-3" @click.prevent="showPlaylistDetails = true">
                {{ i }}
              </a>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-7">
        <div class="card shadow-sm">
          <div class="card-body">
          </div>
        </div>

        <div class="row mt-5">
          <div class="col-12">
            <router-link :to="{ name: 'video_details', params: { id: 'vd_sinefozineo' } }">
              <div v-for="i in 100" :key="i" class="card shadow-sm mb-2">
                <div class="card-body p-2">
                  <div class="d-flex justify-content-around align-items-center">
                    <div class="video">
                      <v-img src="/avatar3.png" width="140"></v-img>
                    </div>
                    <div class="information">
                      <h3 class="h4">Video title</h3>
                      <router-link :to="{ name: 'channel_details', params: { id: 'ch_noienozinfoz' } }" aria-label="">
                        <p class="fw-bold">The creator account</p>
                      </router-link>
                      <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit.</p>
                    </div>
                  </div>
                </div>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- Modals -->
    <v-dialog v-model="showCreatePlaylist" max-width="500" @close="showCreatePlaylist = false">
      <v-card>
        <v-card-text>
          <v-form @submit.prevent>
            <v-text-field placeholder="Playlist name" variant="outlined"></v-text-field>
            <v-switch label="Private" inset hide-details></v-switch>
            <div v-show="isIntelligent" id="intelligent-functionnalities" class="mt-4">
              <div class="d-flex gap-2">
                <v-select :items="videoDetails" variant="outlined"></v-select>
                <v-select placeholder="Operator" variant="outlined"></v-select>
                <v-text-field placeholder="Value" variant="outlined"></v-text-field>
              </div>
            </div>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-btn @click="showCreatePlaylist = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </section>
</template>

<script>
import { ref } from 'vue'

const videoDetails = [
  'Name',
  'Author',
  'Release Date'
]

export default {
  setup () {
    const showCreatePlaylist = ref(false)
    const isIntelligent = ref(false)
    const showPlaylistDetails = ref(false)
    return {
      showPlaylistDetails,
      videoDetails,
      showCreatePlaylist,
      isIntelligent
    }
  },
  watch: {
    showCreatePlaylist (n) {
      if (!n) {
        this.isIntelligent = false
      }
    }
  }
}
</script>
