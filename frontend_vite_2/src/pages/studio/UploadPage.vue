<template>
  <section id="uploads">
    <div class="row">
      <div class="col-10 offset-md-1 mb-4">
        <base-stepper :steps="steps" @update:step="(value) => uploadStep = value" />
      </div>
      
      <div class="col-10 offset-md-1">
        <div class="card shadow-sm">
          <keep-alive>
            <component :is="uploadComponents[uploadStep]" @update:file="handleUpdateFile" @update:data="handleChange" @next="increase" @cancel="decrease" />
          </keep-alive>

          <div class="card-footer d-flex justify-content-end gap-2">
            <button v-if="isFinalStep" type="button" class="btn btn-primary" @click="handleUploadVideo">
              Complete
            </button>

            <v-btn v-else variant="tonal" color="dark" rounded @click="increase">
              Next
              <font-awesome-icon icon="arrow-right" class="ms-2" />
            </v-btn>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { FileUploadRequestData } from '@/types/studio';
import { computed, defineComponent, provide, ref } from 'vue';

import BaseStepper from '@/components/BaseStepper.vue';
import FinalizeComponent from '@/components/studio/FinalizeComponent.vue';
import UploadComponent from '@/components/studio/UploadComponent.vue';
import VideoInformationComponent from '@/components/studio/VideoInformationComponent.vue';
import VideoVisibilityComponent from '@/components/studio/VideoVisibilityComponent.vue';

const steps = [
  {
    id: 1,
    title: 'Upload videos'
  },
  {
    id: 2,
    title: 'Information'
  },
  {
    id: 3,
    title: 'Publication'
  },
  {
    id: 4,
    title: 'Finalize'
  }
]

export default defineComponent({
  name: 'UploadPage',
  components: {
    BaseStepper,
    FinalizeComponent,
    UploadComponent,
    VideoInformationComponent,
    VideoVisibilityComponent
  },
  setup () {
    const uploadStep = ref(0)
    const requestData = ref<FileUploadRequestData>({
      video: null,
      title: null,
      description: null,
      channel_playlist: null,
      recording_location: null,
      visibility: true,
      category: null,
      subcategory: null,
      age_restricted: false
    })

    const isFirstStep = computed(() => {
      return uploadStep.value === 0
    })

    const isFinalStep = computed(() => {
      return uploadStep.value === 3
    })

    provide('requestData', requestData)

    return {
      steps,
      isFirstStep,
      isFinalStep,
      uploadStep,
      requestData,
      uploadComponents: [
        'upload-component',
        'video-information-component',
        'video-visibility-component',
        'finalize-component'
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
     * Handle the data coming from the components
     * in order to update the request data property
     */
    handleChange (data: Record<string, string | number>) {
      this.requestData = {...this.requestData, ...data}
    },
    handleUpdateFile (data: File) {
      this.requestData.video = data
      this.increase()
    },
    /**
     * 
     */
    async handleUploadVideo () {
      try {
        if (this.requestData.video) {
          const form = new FormData()
          form.append('video', this.requestData.video)

          if (this.requestData.title) {
            form.append('title', this.requestData.title)
          }
          
          form.append('description', this.requestData.description || '')
          form.append('channel_playlist', this.requestData.channel_playlist || '')
          form.append('recording_location', this.requestData.recording_location || '')
  
          await this.$client.post('/videos/studio/upload', form, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
        } else {
          console.error('There is no video')
        }
        this.$router.push({ name: 'my_studio' })
      } catch {
        // Handle error
      }
    }
  }
})
</script>
