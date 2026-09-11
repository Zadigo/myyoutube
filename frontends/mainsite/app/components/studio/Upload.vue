<template>
  <div class="text-center">
    <u-file-upload type="file" label="Upload your video" accept=".mp4,.flv" multiple />
  </div>
</template>

<script lang="ts" setup>
const emit = defineEmits<{ 'update:file': [data: File[]], callback: () => void }>()

const studioStore = useStudioStore()

const { data } = useWebSocket(`${useRuntimeConfig().public.apiUploads}/ws/uploads`, {
  immediate: true,
  onConnected() {}
})
</script>
