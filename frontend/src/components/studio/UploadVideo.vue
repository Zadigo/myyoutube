<template>
  <div class="card text-center">
    <div class="card-body">
      <div class="file-uploader">
        <input id="video" type="file" class="form-control" multiple accept=".mp4,.flv" @change="upload($event)">
        <!-- <base-input id="video" input-type="file" multiple @update:initial="upload($event)" /> -->

        <label for="video">
          <div id="start">
            <font-awesome-icon icon="fa-solid fa-upload" size="4x" aria-hidden="true" />
            <div class="mt-3 text-muted">Select a file or drag here</div>
            <span class="btn btn-primary mt-4">Select files</span>
          </div>
        </label>
      </div>
    </div>
  
    <div class="card-footer">
      <p class="my-3 text-muted">
        By submitting your videos to YouTube, you acknowledge that you agree to YouTube's Terms of Service and Community Guidelines.
        Please be sure not to violate others' copyright or privacy rights. Learn more
      </p>
    </div>
  </div>
</template>

<script>
import { useStudio } from '@/store/studio'

// import BaseInput from '@/layouts/bootstrap/BaseInput.vue'

export default {
  name: 'UploadVideo',
  components: {
    // BaseInput
  },
  emits: {
    'next': () => true
  },
  setup () {
    const store  = useStudio()
    return {
      store
    }
  },
  methods: {
    upload (e) {
      this.store.videosToUpload = e.target.files
      this.$emit('next', e.target.files)
    }
  }
}
</script>

<style scoped>
.file-uploader {
  display: block;
  clear: both;
  margin: 0 auto;
  width: 100%;
  max-width: 600px;
}

.file-uploader label {
  float: left;
  clear: both;
  width: 100%;
  padding: 2rem 1.5rem;
  text-align: center;
  background: #fff;
  border-radius: 7px;
  border: 3px solid #f8f9fa;
  transition: all 0.2s ease;
  cursor: pointer;
}

.file-uploader label:hover {
  /* border-color: #1266f1; */
  background-color: #f8f9fa;
  border-color: #c6c7c8;
}

.file-uploader input[type=file] {
  display: none;
}
</style>
