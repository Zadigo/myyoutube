<template>
  <div class="card-body">
    <div class="row">
      <div class="col-7">
        <v-text-field v-model="returnData.title" type=" text" placeholder="Title" variant="outlined" @keypress="handleChange"></v-text-field>
        <textarea v-model="returnData.description" cols="30" rows="7" class="form-control my-1" placeholder="Description" @keypress="handleChange"></textarea>
      </div>

      <div class="col-5">
        <base-video-player :video-url="store.previewUrl" :revoke-url="true" @loaded-meta-data="handleFrameInformation" />
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
  </div>
</template>

<script>
import { ref } from 'vue'
import BaseVideoPlayer from 'src/components/BaseVideoPlayer.vue'

export default {
  name:'VideoInformation',
  components: {
    BaseVideoPlayer
  },
  emits: {
    'update:data' () {
      return true
    }
  },
  setup () {
    const store = {}
    const frames = ref(null)

    const returnData = ref({
      title: null,
      description: null
    })

    return {
      store,
      returnData,
      frames
    }
  },
  methods: {
    handleFrameInformation () {
      
    },
    handleChange () {
      this.$emit('update:data', this.returnData)
    }
  }
}
</script>
