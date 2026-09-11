<template>
  <section id="uploads" class="container mx-auto px-5">
    <u-card class="shadow-sm">
      <u-stepper orientation="vertical" :items="items">
        <template #content="{ item }">
          <div class="max-w-4xl mx-auto">
            <transition 
              mode="out-in" 
              enter-active-class="transition-all ease-in-out duration-200" 
              leave-active-class="transition-all ease-in-out duration-200" 
              enter-from-class="opacity-0 translate-x-10" 
              enter-to-class="opacity-100" 
              leave-from-class="opacity-100" 
              leave-to-class="opacity-0"
            >
              <lazy-studio-upload v-if="item.title === 'Upload video'" hydrate-on-visible />
              <lazy-studio-video-information v-else-if="item.title === 'Video Information'" hydrate-on-visible />
              <lazy-studio-video-visibility v-else-if="item.title === 'Visibility'" hydrate-on-visible />
              <lazy-studio-finalize v-else-if="item.title === 'Finalize'" hydrate-on-visible />
            </transition>
          </div>
        </template>
      </u-stepper>

      <template #footer>
        <u-button :disabled="!isFinalStep" @click="studioStore.submit">
          Complete
        </u-button>
      </template>
    </u-card>
  </section>
</template>

<script lang="ts" setup>
import type { StepperItem } from '@nuxt/ui'

const studioStore = useStudioStore()
const { newVideo } = storeToRefs(studioStore)

const activeStep = ref<number>(1)
const isFinalStep = computed(() => activeStep.value === 4)

const items = ref<StepperItem[]>([
  {
    title: 'Upload video',
    description: 'Upload your video file here',
    icon: 'i-lucide-house'
  },
  {
    title: 'Video Information',
    description: 'Provide details about your video',
    icon: 'i-lucide-info'
  },
  {
    title: 'Visibility',
    description: 'Set the visibility of your video',
    icon: 'i-lucide-eye'
  },
  {
    title: 'Finalize',
    description: 'Finalize your video upload',
    icon: 'i-lucide-check-circle'
  }
])
</script>
