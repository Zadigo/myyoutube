<template>
  <div class="text-center">
    <div class="file-uploader border-2 border-dashed border-primary-800 rounded-lg p-5 hover:border-primary hover:bg-slate-50 transition-colors cursor-pointer" @drop.prevent="handleDrop" @dragover.prevent="handleDragOver" @dragleave.prevent="handleDragLeave">
      <input id="video" type="file" class="form-control hidden" multiple accept=".mp4,.flv" @change="($event) => handleUpload($event)">

      <label for="video">
        <div id="start">
          <Icon name="i-fa7-solid:upload" class="text-5xl" aria-hidden="true" />
          <div class="mt-3 text-muted">
            Select a file or drag here
          </div>

          <p v-if="selectedFiles.length > 0" class="text-secondary">
            {{ formatFileSize(selectedFiles[0]?.size) }}
          </p>

          <VoltButton :badge="selectedFiles.length.toString()" label="Select files" class="mt-4" />
        </div>
      </label>
    </div>
  </div>
</template>

<script lang="ts" setup>
const emit = defineEmits<{ 'update:file': [data: File[]], callback: () => void }>()

const maxSize = 500 * 1024 * 1024
const selectedFiles = ref<File[]>([])

const studioStore = useStudioStore()

async function requestPreviewFile () {
  // Upload the file to the backend so
  // that we can get information on the
  // video that the user is trying to upload
  
}

/**
 * Formats the file size into a human-readable string
 * @param bytes Number of bytes
 */
function formatFileSize(bytes: number | undefined | null): string {
  if (!bytes || bytes === 0) {
    return '0 Bytes'
  }

  const k = 1024
  const sizes = ['Bytes', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return `${parseFloat((bytes / Math.pow(k, i)).toFixed(2))} ${sizes[i]}`
}

/**
 * This function handles the files selected by the user
 * @param files FileList
 */
function handleFiles (files: FileList) {
  const validFiles = Array.from(files).filter(file => {
    if (!file.type.includes('video/')) {
      console.error('Please upload only video files')
      return false
    }
    
    if (file.size > maxSize) {
      console.error(`File size should not exceed ${formatFileSize(maxSize)}`)
      return false
    }
    
    return true
  })
  
  studioStore.newVideo.files = validFiles
}

/**
 * This function handles the file upload when the user selects files
 * @param e Event
 */
function handleUpload (e: Event) {
  const input = e.target as HTMLInputElement

  if (input.files) {
    handleFiles(input.files)
  }
}

const isDragging = ref<boolean>(false)

function handleDrop(event: DragEvent) {
  isDragging.value = false
  if (event.dataTransfer?.files) {
    handleFiles(event.dataTransfer.files)
  }
}

function handleDragOver() {
  isDragging.value = true
}

function handleDragLeave() {
  isDragging.value = false
}

function removeFile(file: File) {
  selectedFiles.value = selectedFiles.value.filter(f => f !== file)
  emit('update:files', selectedFiles.value)
}
</script>
