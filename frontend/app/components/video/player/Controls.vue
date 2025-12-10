<template>
  <div class="absolute bottom-5 bg-primary-500/30 dark:bg-primary-900/30 p-5 max-w-2xl text-primary-50 dark:text-primary rounded-md shadow-sm z-50">
    <div class="grid grid-cols-2">
      <div class="col-span-2">
        <div class="py-5">
          <client-only>
            <volt-slider v-model="sliderValue" :min="0" :max="100" />
          </client-only>
        </div>
      </div>

      <div class="flex justify-left items-center gap-3">
        <volt-button @click.stop="emit('play-pause')">
          <icon v-if="!isPlaying" name="i-fa7-solid:play" />
          <icon v-else name="i-fa7-solid:pause" />
        </volt-button>

        <div class="video-control-duration mx-3">
          <span>{{ currentTime }}</span> /
          <span>{{ durationTime }}</span>
        </div>
      </div>

      <!-- Control configuration center -->
      <div class="flex justify-end gap-2">
        <div id="video-control-settings">
          <volt-button @click="() => emit('show:settings')">
            <icon name="i-fa7-solid:cog" />
          </volt-button>
        </div>

        <div id="video-control-volume" class="ms-2">
          <volt-button @click="() => emit('show:volume')">
            <icon v-if="volume < 0.1" name="i-fa7-solid:volume-low" />
            <icon v-else-if="volume >= 0.1 && volume <= 0.8" name="i-fa7-solid:volume-up" />
            <icon v-else-if="volume > 0.8" name="i-fa7-solid:volume-high" />
          </volt-button>
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
  set: (value) => { console.log('Set slider to:', value) }
})
</script>
