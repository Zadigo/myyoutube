<template>
  <div class="card-body text-center">
    <ClientOnly>
      <div class="file-uploader border-2 border-dashed rounded-lg p-5 hover-border-primary transition-colors" @drop.prevent="handleDrop" @dragover.prevent="isDragging=true" @dragleave.prevent="isDragging=false">
        <input id="video" type="file" class="form-control d-none" multiple accept=".mp4,.flv" @change="handleUpload($event)">

        <label for="video">
          <div id="start">
            <font-awesome icon="upload" size="4x" aria-hidden="true" />
            <div class="mt-3 text-muted">
              Select a file or drag here
            </div>

            <p v-if="selectedFiles.length > 0" class="text-secondary">
              {{ formatFileSize(selectedFiles[0].size) }}
            </p>

            <span class="btn btn-primary btn-rounded mt-4">
              Select files <span class="badge badge-light ms-2">{{ selectedFiles.length }}</span>
            </span>
          </div>
        </label>
      </div>
    </ClientOnly>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const emit = defineEmits({
  'update:file': (_data: File[]) => true
})

const isDragging = ref(false)
const maxSize = 500 * 1024 * 1024
const fileToUpload = ref<HTMLInputElement | null>(null)
const selectedFiles = ref<File[]>([])

async function requestPreviewFile () {
  // Upload the file to the backend so
  // that we can get information on the
  // video that the user is trying to upload
  
}

function formatFileSize(bytes: number): string {
  if (bytes === 0) {
    return '0 Bytes'
  }

  const k = 1024
  const sizes = ['Bytes', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return `${parseFloat((bytes / Math.pow(k, i)).toFixed(2))} ${sizes[i]}`
}

function validateFile(file: File): boolean {
  if (!file.type.includes('video/')) {
    console.error('Please upload only video files')
    return false
  }
  
  if (file.size > maxSize) {
    console.error(`File size should not exceed ${formatFileSize(maxSize)}`)
    return false
  }
  
  return true
}

function handleFiles (files: FileList) {
  const validFiles = Array.from(files).filter(validateFile)
  selectedFiles.value = validFiles
  emit('update:file', selectedFiles.value)
}

function handleUpload (e: Event) {
  const input = e.target as HTMLInputElement

  if (input.files) {
    handleFiles(input.files)
  }
}

function handleDrop(event: DragEvent) {
  isDragging.value = false
  if (event.dataTransfer?.files) {
    handleFiles(event.dataTransfer.files)
  }
}

function removeFile(file: File) {
  selectedFiles.value = selectedFiles.value.filter(f => f !== file)
  emit('update:files', selectedFiles.value)
}
</script>
