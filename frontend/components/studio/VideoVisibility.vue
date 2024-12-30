<template>
  <div class="card-body">
    <div class="row">
      <div class="col-12">
        <p class="fw-bold">
          Age restriction
        </p>
        
        <div class="text-muted">
          <p class="fw-bold">
            Do you want to restrict your video to an adult audience?
          </p>
          <p class="fw-light">
            Age-restricted videos are not shown in certain areas of YouTube. 
            These videos may have limited or no ads monetization
          </p>
        </div>
        
        <v-switch v-model="requestData.age_restricted" :label="ageRestrictedLabel" inset />      
      </div>

      <div class="col-12">
        <p class="fw-bold">
          Visibility
        </p>

        <p class="text-muted">
          Choose when to publish
        </p>

        <v-date-picker />
      </div>
    </div>
    
    <v-switch v-model="requestData.visibility" label="Public" inset />
  </div>
</template>

<script lang="ts" setup>
import type { FileUploadRequestData } from '~/types/studio';
import { inject } from 'vue';

const requestData = inject<FileUploadRequestData>('requestData')

const ageRestrictedLabel = computed(() => {
  if (requestData?.age_restricted) {
    return 'Yes, restrict my video to viewers over 18'
  } else {
    return "No, don't restrict my video to viewers over 18 only"
  }
})
</script>
