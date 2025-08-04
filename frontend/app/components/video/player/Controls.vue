<template>
  <div class="absolute bottom-1/12 bg-primary-900/30 p-5 max-w-2xl text-white rounded-md shadow-sm z-50">
    <div class="grid grid-cols-2">
      <div class="col-span-2">
        <div class="py-5">
          <VoltSlider v-model="sliderValue" :min="0" :max="100" />
        </div>
      </div>

      <div class="flex justify-left items-center gap-3">
        <VoltButton @click.stop="emit('play-pause')">
          <Icon v-if="!isPlaying" name="i-fa7-solid:play" />
          <Icon v-else name="i-fa7-solid:pause" />
        </VoltButton>

        <div class="video-control-duration mx-3">
          <span>{{ currentTime }}</span> /
          <span>{{ durationTime }}</span>
        </div>
      </div>

      <!-- Control configuration center -->
      <div class="flex justify-end gap-2">
        <div id="video-control-settings">
          <VoltButton @click="() => emit('show:settings')">
            <Icon name="i-fa7-solid:cog" />
          </VoltButton>
        </div>

        <div id="video-control-volume" class="ms-2">
          <VoltButton @click="() => emit('show:volume')">
            <Icon v-if="volume < 0.1" name="i-fa7-solid:volume-low" />
            <Icon v-else-if="volume >= 0.1 && volume <= 0.8" name="i-fa7-solid:volume-up" />
            <Icon v-else-if="volume > 0.8" name="i-fa7-solid:volume-high" />
          </VoltButton>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const emit = defineEmits<{ 'play-pause': [], 'show:volume': [], 'show:settings': [] }>()
const { volume = 0.1, currentTime = '00:00', durationTime = '00:00', isPlaying = false } = defineProps<{ volume?: number, currentTime?: string, durationTime?: string, isPlaying?: boolean }>()

const showVolume = ref<boolean>(false)
const showSpeedSettings = ref<boolean>(false)
const showInteractiveMenu = ref<boolean>(false)
const showVideoSettings = ref<boolean>(true)
const showQualitySettings = ref<boolean>(true)

const completionPercentage = inject<Ref<number>>('completionPercentage')

const sliderValue = computed({
  get: () => completionPercentage?.value || 0,
  set: (value) => {}
})
</script>
