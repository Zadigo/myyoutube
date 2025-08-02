<template>
  <section id="uploads">
    <div class="row">
      <div class="col-10 offset-md-1 mb-4">
        <BaseStepper :steps="steps" @update:step="(value) => uploadStep = value" />
      </div>
      
      <div class="col-10 offset-md-1">
        <div class="card shadow-sm">
          <KeepAlive>
            <component :is="uploadComponents[uploadStep]" @update:file="handleUpdateFile" @update:data="handleChange" @next="increase" @cancel="decrease" />
          </KeepAlive>

          <div class="card-footer d-flex justify-content-end gap-2">
            <button v-if="isFinalStep" type="button" class="btn btn-primary" @click="handleUploadVideo">
              Complete
            </button>

            <v-btn v-else variant="tonal" color="dark" rounded @click="increase">
              Next
              <font-awesome icon="arrow-right" class="ms-2" />
            </v-btn>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts" setup>
import { computed, provide, ref } from 'vue';
import type { FileUploadRequestData } from '~/apps/types';

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

const router = useRouter()
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


const { $client } = useNuxtApp()
const UploadComponent = resolveComponent('StudioUpload')
const FinalizeComponent = resolveComponent('StudioFinalize')
const VideoInformationComponent = resolveComponent('StudioVideoInformation')
const VideoVisibilityComponent = resolveComponent('StudioVideoVisibility')

const uploadComponents = [
  UploadComponent,
  VideoInformationComponent,
  VideoVisibilityComponent,
  FinalizeComponent
]

const isFirstStep = computed(() => {
  return uploadStep.value === 0
})

const isFinalStep = computed(() => {
  return uploadStep.value === 3
})

provide('requestData', requestData)

/**
 * 
 */
function increase () {
  uploadStep.value = uploadStep.value + 1
}

/**
 * 
 */
function decrease () {
  uploadStep.value = uploadStep.value - 1
}

/**
 * Handle the data coming from the components
 * in order to update the request data property
 */
function handleChange (data: Record<string, string | number>) {
  requestData.value = {...requestData.value, ...data}
}

function handleUpdateFile (data: File) {
  requestData.value.video = data
  increase()
}

/**
 * 
 */
async function handleUploadVideo () {
  try {
    if (requestData.value.video) {
      const form = new FormData()
      // TODO: Allow uploading of multiple videos
      form.append('video', requestData.value.video[0])

      if (requestData.value.title) {
        form.append('title', requestData.value.title)
      }
      
      form.append('description', requestData.value.description || '')
      form.append('channel_playlist', requestData.value.channel_playlist || '')
      form.append('recording_location', requestData.value.recording_location || '')

      await $client.post('/videos/studio/upload', form, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
    } else {
      console.error('There is no video')
    }
    router.push('/studio')
  } catch {
    // Handle error
  }
}
</script>
