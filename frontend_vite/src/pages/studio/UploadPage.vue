<template>
  <section id="uploads">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <component :is="uploadComponents[uploadStep]" @update:data="handleChange" @next="increase" @cancel="decrease" />

          <div class="card-footer">
            <button type="button" class="btn btn-primary" @click="decrease">Previous</button>
            <button type="button" class="btn btn-primary" @click="increase">Next</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref } from 'vue'
import UploadComponent from '../../components/studio/UploadComponent.vue'
import VideoInformationComponent from '../../components/studio/VideoInformationComponent.vue'
import VideoVisibilityComponent from '../../components/studio/VideoVisibilityComponent.vue'

export default {
  name: 'UploadPage',
  components: {
    UploadComponent,
    VideoInformationComponent,
    VideoVisibilityComponent
  },
  setup () {
    const uploadStep = ref(0)
    const requestData = ref({
      video: null,
      title: null,
      description: null
    })

    return {
      uploadStep,
      requestData,
      uploadComponents: [
        'upload-component',
        'video-information-component',
        'video-visibility-component'
      ]
    }
  },
  methods: {
    increase () {
      this.uploadStep = this.uploadStep + 1
    },
    decrease () {
      this.uploadStep = this.uploadStep - 1
    },
    handleChange (data) {
      this.requestData = {...this.requestData, ...data}
    }
  }
}
</script>
