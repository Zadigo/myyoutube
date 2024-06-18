<template>
  <div class="card-body text-center">
    <div class="file-uploader">
      <input id="video" type="file" class="form-control" multiple accept=".mp4,.flv" @change="handleUpload($event)">

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

<script>
import { ref } from 'vue'

export default {
  name: 'UploadComponent',
  emits: {
    'next': () => true
  },
  setup () {
    const fileToUpload = ref(null)
    return {
      fileToUpload
    }
  },
  methods: {
    handleUpload (e) {
      this.fileToUpload = e.target.files
      this.$emit('next', e.target.files)
    }
  }
}
</script>
