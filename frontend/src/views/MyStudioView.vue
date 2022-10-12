<template>
  <base-site-vue>
    <section id="my-studio">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12 mb-2">
            <component :is="stages[index]" @next="increase" @cancel="decrease" />
          </div>

          <div class="col-12">
            <div class="card">
              <div class="card-header d-flex justify-content-left">
                <button type="button" class="btn btn-md btn-primary me-2">Button</button>
                <div class="input-group">
                  <input v-model="search" :placeholder="$t('Search')" type="text" class="form-control p-2">
                  <button id="button-addon1" class="btn btn-outline-secondary" type="button">Button</button>
                </div>
              </div>
              
              <div class="card-body">
                <div class="list-group">
                  <a v-for="video in searchedVideos" :key="video.id" :class="[videoSelected(item) ? 'active' : null]" href class="list-group-item list-group-item-action p-4 d-flex gap-4 justify-content-left align-items-center" @click.prevent="selectVideo(video)">
                    <img src="https://via.placeholder.com/100x100" class="img-fluid rounded" alt="">
                    
                    <div class="infos p-2">
                      <h5>Quick title</h5>

                      <p class="mb-2">
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ratione error alias 
                        voluptatibus doloremque adipisci, inventore quas? Ipsum commodi
                      </p>
                      
                      <p class="d-flex justify-content-left text-muted">
                        <span>{{ $t('x views', { count: 4456}) }}</span> -
                        <span class="mx-2">400 likes</span>
                      </p>
                    </div>
                    
                    <div class="btn-group shadow-none">
                      <button id="button-addon1" class="btn btn-secondary" type="button">
                        <font-awesome-icon icon="fa-solid fa-pen" />
                      </button>
                      <button id="button-addon1" class="btn btn-secondary" type="button">Button</button>
                    </div>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </base-site-vue>
</template>

<script>
import _ from 'lodash'
import { useUtilities } from '@/composables/utils'

import BaseSiteVue from '@/layouts/BaseSite.vue'
import BaseCheckbox from '@/layouts/bootstrap/BaseCheckbox.vue'
import UploadVideo from '@/components/studio/UploadVideo.vue'
import VideoInfo from '@/components/studio/VideoInfo.vue'
import VideoVisibility from '@/components/studio/VideoVisibility.vue'

export default {
  name: 'MyStudioView',
  components: {
    BaseSiteVue,
    BaseCheckbox,
    VideoInfo,
    UploadVideo,
    VideoVisibility
  },
  setup () {
    const { listManager } = useUtilities()
    return {
      listManager
    }
  },
  data () {
    return {
      video: null,
      index: 0,
      stages: [
        'upload-video',
        'video-info',
        'video-visibility'
      ],
      search: null,
      selectedVideos: []
    }
  },
  computed: {
    searchedVideos () {
      if (this.search) {
        return _.filter([{ id: 1 }, { id: 3 }, { id: 4 }], (video) => {
          return video.id === this.search
        })
      } else {
        return [{ id: 1 }, { id: 3 }, { id: 4 }]
      }
    }
  },
  methods: {
    increase () {
      this.index = this.index + 1
    },
    decrease () {
      this.index = this.index - 1
    },
    selectVideo (item) {
      this.selectedVideos = this.listManager(this.selectedVideos, item)
    },
    videoSelected (item) {
      return _.some(_.map(this.selectedVideos, (video) => {
        return video.id === item.id
      }))
    }
  }
}
</script>

<style scoped>
</style>
