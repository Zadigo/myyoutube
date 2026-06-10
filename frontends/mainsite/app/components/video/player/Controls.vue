<template>
  <div class="absolute bottom-5 bg-primary-500/30 dark:bg-primary-900/30 p-5 w-full xl:max-w-6xl text-primary-50 dark:text-primary rounded-full shadow-sm z-40">
    <div class="grid grid-cols-12 gap-4">
      <div class="col-span-3 flex justify-left items-center gap-3">
        <volt-button rounded @click.stop="handlePlayPause">
          <icon v-if="!isPlaying" name="i-fa7-solid:play" />
          <icon v-else name="i-fa7-solid:pause" />
        </volt-button>

        <div class="text-sm mx-3">
          <span>{{ currentTimeFormatted }}</span> /
          <span>{{ durationFormatted }}</span>
        </div>
      </div>

      <div class="col-span-7">
        <client-only>
          {{ isPlaying }}
          <volt-slider v-model="sliderValue" :min="0" :max="100" />
        </client-only>
      </div>

      <div class="col-span-2 flex gap-2">
        <div class="ms-auto">
          <volt-button rounded>
            <icon name="i-fa7-solid:cog" />
          </volt-button>
        </div>

        <div>
          <volt-button rounded>
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
import { useVideoPlayerControls, useVideoPlayerOptions, useVideoPlayerStore } from './utils'

defineEmits<{ 'show:settings': [] }>()

const { el } = useVideoPlayerStore()
console.log(el)
const { isPlaying, currentTimeFormatted, durationFormatted, completionPercentage, handlePlayPause } = useVideoPlayerControls(el)
const { volume, quality, speed } = useVideoPlayerOptions(el)

const sliderValue = computed({
  get: () => completionPercentage?.value || 0,
  set: (value) => {
    if (isDefined(el) && isDefined(el.value?.duration)) {
      el.value.currentTime = (value / 100) * el.value.duration
    }
  }
})
</script>
