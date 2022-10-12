<template>
  <div class="card">
    <div class="card-header">
      <h2>Video Info</h2>
    </div>
    
    <div class="card-body">
      <div class="row">
        <div class="col-7">
          <input type="text" class="p-2 form-control" placeholder="Title">
          <textarea cols="30" rows="7" class="form-control my-1" placeholder="Description"></textarea>
        </div>

        <div class="col-5">
          <!-- <base-video-player :video-url="require('@/assets/video3_hd.mp4')" /> -->
          <base-video-player :video-url="store.previewUrl" :revoke-url="true" @loaded-meta-data="getFrame" />
        </div>
      </div>

      <div class="my-3">
        <h5>Thumbnail</h5>
        <p class="text-muted">
          Select or upload a picture that shows what's in your video.
          A good thumbnail stands out and draws viewers'
          attention. Learn more
        </p>
        <div class="row">
          <div v-for="(frame, i) in frames" :key="i" class="col-3">
            <img :src="frame[1]" class="img-fluid" alt="">
          </div>
        </div>
      </div>
      
      <div class="my-3">
        <h5>series</h5>
        <p class="text-muted mb-2">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi voluptatem ab 
          temporibus nobis. Velit tempore provident natus unde eos iusto, autem sint dignissimos 
          numquam ipsum labore maxime? Omnis, recusandae soluta!
        </p>
        <base-checkbox id="series" label="This video is part of a series" class="my-3" />
        <input type="text" class="p-2 mb-2 form-control" placeholder="series name">
        <input type="text" class="p-2 form-control" placeholder="season">
      </div>

      <div class="my-3">
        <h5>Paid promotion</h5>
        <p class="text-muted">
          If you accepted anything of value from a third party to make your video,
          you must let us know. We’ll show viewers a message that tells them your video
          contains paid promotion.
        </p>
        <base-checkbox id="promotion" label="My video contains paid promotion like a product placement, sponsorship, or endorsement" class="my-3" />
        <p class="text-muted fs-small">
          By selecting this box, you confirm that the paid promotion follows our ad policies
          and any applicable laws and regulations. Learn more
        </p>
      </div>
      
      <div class="my-4">
        <h5>Category</h5>
        <p class="text-muted">
          Add your video to a category so viewers can find it more easily. Miscategoriing your video
          will affect the way your content will be shown to users.
        </p>

        <select class="form-select mb-2" aria-label="Default select example">
          <option selected>select a category</option>
          <option value="1">One</option>
          <option value="2">Two</option>
          <option value="3">Three</option>
        </select>
    
        <select class="form-select" aria-label="Default select example">
          <option selected>select a subcategory</option>
          <option value="1">One</option>
          <option value="2">Two</option>
          <option value="3">Three</option>
        </select>
      </div>
      
      <div class="my-4">
        <h5>Tags</h5>
        <input type="text" class="p-2 form-control" placeholder="Tags">
      </div>
      
      <div class="my-4">
        <h5>Language</h5>
        <p class="text-muted">
          Select your video's language
        </p>
        <select class="form-select" aria-label="Default select example">
          <option selected>select a subcategory</option>
          <option value="1">One</option>
          <option value="2">Two</option>
          <option value="3">Three</option>
        </select>
      </div>
      
      <div class="my-4">
        <h5>Recording date and location</h5>
        <p class="text-muted">
          Add when and where your video was recorded. Viewers can search for videos by location.
        </p>
    
        <div class="d-flex justify-content-between">
          <input :max="dayjs().format('YYYY-MM-DD')" type="date" class="p-2 form-control" placeholder="Recording date">
          <input type="text" class="p-2 ms-2 form-control" placeholder="Location">
        </div>
      </div>
      
      <div class="my-4">
        <h5>License</h5>
      </div>

      <div class="my-4">
        <h5>Comments and ratings</h5>
        <p class="text-muted">Choose if and how you want to show comments</p>
        <div class="form-check">
          <input id="allow-all" class="form-check-input" type="radio" name="comment" checked>
          <label class="form-check-label" for="allow-all">
            Allow all comments
          </label>
        </div>
        <div class="form-check">
          <input id="hold-all" class="form-check-input" type="radio" name="comment">
          <label class="form-check-label" for="hold-all">
            Hold all comments for review
          </label>
        </div>
        <div class="form-check">
          <input id="disable-all" class="form-check-input" type="radio" name="comment">
          <label class="form-check-label" for="diable-all">
            Disable comments
          </label>
        </div>
      </div>
    </div>

    <div class="card-footer">
      <button type="button" class="btn btn-lg btn-primary" @click="$emit('cancel')">
        Cancel
      </button>
      <button type="button" class="btn btn-lg btn-primary" @click="$emit('next')">
        Next
      </button>
    </div>
  </div>
</template>

<script>
import { useUtilities } from '@/composables/utils'
import { useStudio } from '@/store/studio'
import dayjs from '@/plugins/dayjs'

import BaseCheckbox from '@/layouts/bootstrap/BaseCheckbox.vue'
import BaseVideoPlayer from '@/layouts/BaseVideoPlayer.vue'

export default {
  name: 'VideoInfo',
  components: {
    BaseCheckbox,
    BaseVideoPlayer
  },
  emits: {
    'cancel': () => true,
    'next': () => true
  },
  setup () {
    const store = useStudio()
    const { readVideoFile, getVideoFrame } = useUtilities()
    return {
      store,
      dayjs,
      getVideoFrame,
      readVideoFile
    }
  },
  data () {
    return {
      frames: []
    }
  },
  beforeMount () {
    this.readFile()
  },
  methods: {
    readFile () {
      const url = this.readVideoFile(this.store.videosToUpload)
      this.store.previewUrl = url
    },
    getFrame (video) {
      const data = this.getVideoFrame(video)
      this.frames.push(data)
      console.log(data)
    }
  }
}
</script>

<style scoped>

</style>
