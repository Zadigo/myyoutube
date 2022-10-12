<template>
  <div class="card text-center">
    <div class="card-body">
      <input id="video" type="file" multiple @change="upload($event)">
    </div>
  
    <div class="card-footer">
      <p class="m-0 text-muted">
        By submitting your videos to YouTube, you acknowledge that you agree to YouTube's Terms of Service and Community Guidelines.
      </p>
      <p class="text-muted">
        Please be sure not to violate others' copyright or privacy rights. Learn more
      </p>
    </div>
  </div>
</template>

<script>
import { useStudio } from '@/store/studio'

export default {
  name: 'UploadVideo',
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

</style>
