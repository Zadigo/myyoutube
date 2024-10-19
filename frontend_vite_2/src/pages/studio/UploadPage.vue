<template>
  <section id="uploads">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <component :is="uploadComponents[uploadStep]" @update:data="handleChange" @next="increase" @cancel="decrease" />

          <div class="card-footer">
            <button :disabled="isFirstStep" type="button" class="btn btn-primary" @click="decrease">
              Previous
            </button>
            
            <button v-if="isFinalStep" type="button" class="btn btn-primary">
              Complete
            </button>

            <button v-else type="button" class="btn btn-primary" @click="increase">
              Next
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from 'vue'

import UploadComponent from '@/components/studio/UploadComponent.vue'
import VideoInformationComponent from '@/components/studio/VideoInformationComponent.vue'
import VideoVisibilityComponent from '@/components/studio/VideoVisibilityComponent.vue'

export default defineComponent({
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

    const isFinalStep = computed(() => {
      return uploadStep.value === 3
    })

    const isFirstStep = computed(() => {
      return uploadStep.value === 0
    })

    return {
      isFirstStep,
      isFinalStep,
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
    /**
     * 
     */
    increase () {
      this.uploadStep = this.uploadStep + 1
    },
    /**
     * 
     */
    decrease () {
      this.uploadStep = this.uploadStep - 1
    },
    /**
     * 
     */
    handleChange (data) {
      console.log(data)
      this.requestData = {...this.requestData, ...data}
    }
  }
})
</script>
