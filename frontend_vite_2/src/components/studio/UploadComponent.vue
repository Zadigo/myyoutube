<template>
  <div class="card-body text-center">
    <div class="file-uploader">
      <input id="video" type="file" class="form-control d-none" multiple accept=".mp4,.flv" @change="handleUpload($event)">

      <label for="video">
        <div id="start">
          <font-awesome-icon icon="fa-solid fa-upload" size="4x" aria-hidden="true" />
          <div class="mt-3 text-muted">Select a file or drag here</div>
          <span class="btn btn-primary mt-4">Select files</span>
        </div>
      </label>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'UploadComponent',
  emits: {
    'next': () => true
  },
  setup () {
    const fileToUpload = ref<HTMLInputElement | null>(null)
    return {
      fileToUpload
    }
  },
  methods: {
    async requestPreviewFile () {
      // Upload the file to the backend so
      // that we can get information on the
      // video that the user is trying to upload
      
    },
    handleUpload (e: Event) {
      if (e) {
        this.fileToUpload = <HTMLInputElement>e.target?.files
        this.$emit('next', e.target.files)
      }
    }
  }
})
</script>
