<template>
  <div ref="videoContainerEl" class="relative z-30 flex items-center justify-center cursor-pointer bg-primary-900 mx-auto overflow-hidden">
    <video ref="videoPlayerEl" class="h-full w-full touch-manipulation has-[source]:h-full" preload="metadata" controlist="nodownload" oncontextmenu="return false;" @loadedmetadata="handleVideoMetadata" @timeupdate="handleVideoMetadata" @canplay="handleCanPlay" @click.stop="handlePlayPause">
      <source :src="videoSource" type="video/mp4">
    </video>

    <DevOnly>
      <div class="p-5 rounded-md absolute top-1/6 max-w-xs z-50 bg-primary-50/80 text-primary-900">
        {{ playingDetails }}
      </div>
    </DevOnly>

    <!-- Controls -->
    <VideoPlayerControls :current-time="currentTimeFormatted" :duration-time="durationFormatted" :is-playing="isPlaying" :volume="volume" @play-pause="handlePlayPause" />
  </div>
</template>

<script setup lang="ts">
import type { VideoTechnicalDetails } from '~/types' 

defineProps<{ videoSource: string }>()

const emit = defineEmits<{ 
  'play': [], 
  'pause': [VideoTechnicalDetails], 
  'player:loaded': [], 
  'update:metadata': [data: VideoTechnicalDetails] 
}>()

const speeds = [2, 1.75, 1.5, 1, 0.75, 0.5] as const

type Speeds  = (typeof speeds)[number]

const isLoading = ref<boolean>(true)
const isPlaying = ref<boolean>(false)

const duration = ref<number>(0)
const currentTime = ref<number>(0)
const volume = ref<number>(0.5)

const speed = ref<string>('1x')
const quality = ref<string>('1080p')

const videoContainerEl = useTemplateRef('videoContainerEl')
const videoPlayerEl = useTemplateRef('videoPlayerEl')

onBeforeUnmount(() => {
  if (videoPlayerEl.value) {
    const source = videoPlayerEl.value.querySelector('source')
    
    if (source) {
      URL.revokeObjectURL(source.src)
    }
  }
})

/**
 * Formats the time to a human readable
 * format for the user to track the
 * time at which the video is currently at
 * @param value - The time in seconds to format
 */
function formatTime (value: number) {
  const hours = Math.floor(value / 3600)
  const minutes = Math.floor((value % 3600) / 60)
  const seconds = Math.floor(value % 60)

  const formattedHours = hours < 10 ? '0' + hours : hours
  const formattedMinutes = minutes < 10 ? '0' + minutes : minutes
  const formattedSeconds = seconds < 10 ? '0' + seconds : seconds

  if (hours > 0) {
    return `${formattedHours}:${formattedMinutes}:${formattedSeconds}`
  } else {
    return `${formattedMinutes}:${formattedSeconds}`
  }
}

// Tracks the amount of the times the
// button play was pressed during a
// viewing session
const { count, inc } = useCounter()

const currentTimeFormatted = computed(() => formatTime(currentTime.value))
const durationFormatted = computed(() => formatTime(duration.value))
/**
 * Calculates the current completion of the
 * video in percentage on the total duration
 */
const completionPercentage = computed(() => Math.floor((currentTime.value / duration.value) * 100))

const wasPlayed = ref<boolean>(false)

watchOnce(() => count.value === 1, () => {
  wasPlayed.value = true
})

const playingDetails = computed((): VideoTechnicalDetails => {
  return {
    currentTime: currentTime.value,
    formattedCurrentTime: currentTimeFormatted.value,
    percentagePlayed: completionPercentage.value,
    wasPlayed: wasPlayed.value,
    playPauseCount: count.value
  }
})

onMounted(() => {
  emit('player:loaded')
  emit('update:metadata', playingDetails.value)
})

/**
 * Function that handles the video metadata
 * and updates the duration and current time
 * of the video player
 */
function handleVideoMetadata () {
  if (videoPlayerEl.value) {
    if (!Number.isNaN(videoPlayerEl.value.duration)) {
      duration.value = videoPlayerEl.value.duration
    }

    currentTime.value = videoPlayerEl.value.currentTime
    emit('update:metadata', playingDetails.value)
  }
}

/**
 * Indicates that the video has ended, in other
 * words that the current time is equals the total
 * video duration time
 */
const isEnded = computed(() => currentTimeFormatted.value === durationFormatted.value)

watchOnce(isEnded, () => {
  isPlaying.value = false
  emit('update:metadata', playingDetails.value)
})

provide('completionPercentage', completionPercentage)

// Player state

/**
 * Function that handles the playing
 * and paused states of the player
 */
function handlePlayPause () {
  if (videoPlayerEl.value) {
    if (videoPlayerEl.value.paused) {
      isPlaying.value = true
      videoPlayerEl.value.play()

      inc()
      emit('play')
    } else {
      isPlaying.value = false
      videoPlayerEl.value.pause()
      
      emit('pause', playingDetails.value)
    }
  }
}

/**
 * Handles the canplay event for the video player.
 */
function handleCanPlay () {
  isLoading.value = false
}
</script>
